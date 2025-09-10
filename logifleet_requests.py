import requests
import json
from utils import *

BASE_URL = "https://logifleet360.ch/lfr3/eg-services"
ENDPOINT = "/authenticate"
url = BASE_URL + ENDPOINT


def get_vehicles_and_groups(jwt):

    # VEHICLES
    print("Requesting vehicles...")
    headers = {"Authorization": "Bearer %s" % jwt, "Content-Type": "application/json"}

    response = requests.get(
        BASE_URL + "/api/v2/vehicles",
        headers=headers,
        params={
            "withInactive": "true",  # include the inactive vehicles
            "withDeleted": "true",  # include the deleted vehicles
        },
    )

    vehicles_data = response.json()
    vehicles_df = sort_vehicles(vehicles_data)

    # GROUPS (OF VEHICLES)
    print("Requesting groups...")

    headers = {"Authorization": "Bearer %s" % jwt, "Content-Type": "application/json"}

    group_ids = vehicles_df["groupId"].unique()
    groups_array = []

    for group_id in group_ids:

        response = requests.get(
            BASE_URL + "/api/v2/groups/" + group_id, headers=headers
        )

        if response.status_code == 200:

            groups_data = response.json()
            groups_array.append(
                {
                    "id": groups_data.get("id"),
                    "reference": groups_data.get("reference"),
                    "name": groups_data.get("name"),
                    "description": groups_data.get("description"),
                    "parentGroupName": groups_data.get("parentGroupName"),
                    "parentGroupId": groups_data.get("parentGroupId"),
                    "rootGroup": groups_data.get("rootGroup"),
                }
            )

    groups_df = pd.DataFrame(groups_array)

    return vehicles_df, groups_df


# REPORTS/JOURNEY/DATA


def get_reports(startDate, endDate, jwt):

    print("Requesting reports...")

    headers = {"Authorization": "Bearer %s" % jwt, "Content-Type": "application/json"}

    response = requests.post(
        BASE_URL + "/api/v2/reports/journey/data",
        headers=headers,
        data=json.dumps(
            {
                "startDate": startDate,  # include the inactive vehicles
                "endDate": endDate,  # include the deleted vehicles
            }
        ),
    )

    reports_data = response.json()
    reports_df = sort_reports(reports_data)

    return reports_df
    # reports_df.to_pickle('reports_df.pickle')


# TRIPS


def get_trips(startDate, endDate, jwt):

    # /!\ Max time interval is 1 month!!

    print("Requesting trips...")

    trips_df_per_month = []

    dates = split_into_monthly_ranges(startDate, endDate)

    for date in dates:

        # print(date)
        trips_startDate = date.get("start")
        trips_endDate = date.get("end")

        headers = {
            "Authorization": "Bearer %s" % jwt,
            "Content-Type": "application/json",
        }

        response = requests.post(
            BASE_URL + "/api/v2/trips",
            headers=headers,
            json={
                "startDate": trips_startDate,  # include the inactive vehicles
                "endDate": trips_endDate,  # include the deleted vehicles
            },
        )

        if response.status_code == 200:

            trips_data = response.json()
            monthly_trips_df = sort_trips(trips_data)
            monthly_trips_df["startDate"] = trips_startDate  # pour requête eco score
            monthly_trips_df["endDate"] = trips_endDate  # pour requête eco score
            trips_df_per_month.append(monthly_trips_df)

    trips_df = pd.concat(trips_df_per_month)

    return trips_df


# DASHBOARD/ECODRIVE/V3


def get_scores(startDate, endDate, jwt, trips_df):

    print("Requesting Eco-scores...")

    headers = {"Authorization": "Bearer %s" % jwt, "Content-Type": "application/json"}

    scores_array = []
    for vehicle_id in trips_df["asset_id"].unique():

        response = requests.post(
            BASE_URL + "/api/v2/dashboard/ecoDrive",
            headers=headers,
            data=json.dumps(
                {
                    "vehiclesIds": [vehicle_id],
                    "startDate": startDate,
                    "endDate": endDate,
                    "dimension": "YEAR",
                }
            ),
        )

        if response.status_code == 200:

            scores_json = response.json()

            for s in scores_json:

                vehicle = s.get("vehicle")
                vehicle_id = vehicle.get("id") if vehicle else None
                vehicle_reference = vehicle.get("reference") if vehicle else None
                vehicle_name = vehicle.get("name") if vehicle else None

                group = s.get("group")
                group_id = group.get("id") if group else None
                group_reference = group.get("reference") if group else None
                group_name = group.get("name") if group else None

                category = s.get("category")
                category_id = category.get("id") if category else None
                category_reference = category.get("reference") if category else None
                category_name = category.get("name") if category else None

                scores_array.append(
                    {
                        "vehicle_id": vehicle_id,
                        "vehicle_reference": vehicle_reference,
                        "vehicle_name": vehicle_name,
                        "group_id": group_id,
                        "group_reference": group_reference,
                        "group_name": group_name,
                        "category_id": category_id,
                        "category_reference": category_reference,
                        "category_name": category_name,
                        "driver": s.get("driver"),
                        "globalScore": s.get("globalScore"),
                        "acceleration": s.get("acceleration"),
                        "breaking": s.get("breaking"),
                        "cornering": s.get("cornering"),
                        "distance": s.get("distance"),
                        "timeDimension": s.get("timeDimension"),
                        "drivingDuration": s.get("drivingDuration"),
                        "numberOfTrips": s.get("numberOfTrips"),
                    }
                )

    scores_df = pd.DataFrame(scores_array)
    return scores_df
