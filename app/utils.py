import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime
import locale

# Définir la locale française pour avoir les noms de mois en français
locale.setlocale(locale.LC_TIME, "en_US.UTF-8")


def sort_vehicles(vehicles_json):

    vehicles_array = []
    for v in vehicles_json:

        # nested dictonnaries
        tracker = v.get("tracker")
        tracker_id = tracker.get("id") if tracker else None
        tracker_type = tracker.get("type") if tracker else None
        tracker_oemTrackerType = tracker.get("oemTrackerType") if tracker else None
        tracker_batteryInformation = (
            tracker.get("batteryInformation") if tracker else None
        )
        tracker_availableWiredInputNumber = (
            tracker.get("availableWiredInputNumber") if tracker else None
        )

        vehicleCategory = v.get("vehicleCategory")
        vehicleCategory_id = vehicleCategory.get("id") if vehicleCategory else None
        vehicleCategory_reference = (
            vehicleCategory.get("reference") if vehicleCategory else None
        )
        vehicleCategory_name = vehicleCategory.get("name") if vehicleCategory else None
        vehicleCategory_icon = vehicleCategory.get("icon") if vehicleCategory else None
        vehicleCategory_default = (
            vehicleCategory.get("default") if vehicleCategory else None
        )

        lastUpdatedBy = v.get("lastUpdatedBy")
        lastUpdatedBy_id = lastUpdatedBy.get("id") if lastUpdatedBy else None
        lastUpdatedBy_reference = (
            lastUpdatedBy.get("reference") if lastUpdatedBy else None
        )
        lastUpdatedBy_name = lastUpdatedBy.get("name") if lastUpdatedBy else None

        vehicles_array.append(
            {
                "id": v.get("id"),
                "reference": v.get("reference"),
                "name": v.get("name"),
                "trackerId": tracker_id,
                "trackerType": tracker_type,
                "trackerOemTrackerType": tracker_oemTrackerType,
                "trackerBatteryInformation": tracker_batteryInformation,
                "trackerAvailableWiredInputNumber": tracker_availableWiredInputNumber,
                "groupId": v.get("groupId"),
                "accountId": v.get("account", {}).get("id"),
                "accountReference": v.get("account", {}).get("reference"),
                "accountName": v.get("account", {}).get("name"),
                "active": v.get("active"),
                "deleted": v.get("deleted"),
                "deviceImei": v.get("deviceImei"),
                "vehicleCategoryId": vehicleCategory_id,
                "vehicleCategoryReference": vehicleCategory_reference,
                "vehicleCategoryName": vehicleCategory_name,
                "vehicleCategoryIcon": vehicleCategory_icon,
                "vehicleCategoryDefault": vehicleCategory_default,
                "wiredEquipments": v.get("wiredEquipments"),
                "temperatureEquipments": v.get("temperatureEquipments"),
                "immobilizationEquipment": v.get("immobilizationEquipment"),
                "brand": v.get("brand"),
                "function": v.get("function"),
                "model": v.get("model"),
                "note": v.get("note"),
                "licencePlate": v.get("licencePlate"),
                "serialNumber": v.get("serialNumber"),
                "engineType": v.get("engineType"),
                "subjectToRoadTax": v.get("subjectToRoadTax"),
                "refillPaymentMethod": v.get("refillPaymentMethod"),
                "sizeClassId": v.get("sizeClassId"),
                "purchaseDate": v.get("purchaseDate"),
                "purchasePrice": v.get("purchasePrice"),
                "purchasePriceCurrency": v.get("purchasePriceCurrency"),
                "activeLeasing": v.get("activeLeasing"),
                "dateOfNextService": v.get("dateOfNextService"),
                "lastMaintenanceDate": v.get("lastMaintenanceDate"),
                "currentMileage": v.get("currentMileage"),
                "dashboardOdometer": v.get("dashboardOdometer"),
                "technicalControlMileage": v.get("technicalControlMileage"),
                "idleToDeliverySeconds": v.get("idleToDeliverySeconds"),
                "costPerHour": v.get("costPerHour"),
                "costPerHourUnit": v.get("costPerHourUnit"),
                "costPerKilometer": v.get("costPerKilometer"),
                "costPerKilometerUnit": v.get("costPerKilometerUnit"),
                "inServiceDate": v.get("inServiceDate"),
                "equipmentSetId": v.get("equipmentSetId"),
                "defaultDriver": v.get("defaultDriver"),
                "sharingInformation": v.get("sharingInformation"),
                "maintenanceExpired": v.get("maintenanceExpired"),
                "copyOfSharedVehicle": v.get("copyOfSharedVehicle"),
                "lastUpdatedDate": v.get("lastUpdatedDate"),
                "lastUpdatedBy": v.get("lastUpdatedBy"),
                "lastUpdatedById": lastUpdatedBy_id,
                "lastUpdatedByReference": lastUpdatedBy_reference,
                "lastUpdatedByName": lastUpdatedBy_name,
                "sharedWithProject44": v.get("sharedWithProject44"),
                "attachments": v.get("attachments"),
            }
        )

    return pd.DataFrame(vehicles_array)


def sort_reports(reports_json):

    reports_array = []
    for v in reports_json:

        # nested dictonnaries
        category = v.get("vehicleCategory")
        category_id = category.get("id") if category else None
        category_reference = category.get("reference") if category else None
        category_name = category.get("name") if category else None
        category_icon = category.get("icon") if category else None
        category_default = category.get("default") if category else None

        reports_array.append(
            {
                "id": v.get("id"),
                "dateFormat": v.get("dateFormat"),
                "timeFormat": v.get("dateFormat"),
                "speedUnit": v.get("speedUnit"),
                "distanceUnit": v.get("distanceUnit"),
                "fuelUnit": v.get("fuelUnit"),
                "vehicleId": v.get("vehicleId"),
                "vehicleName": v.get("vehicleName"),
                "vehicleReference": v.get("vehicleReference"),
                "driverId": v.get("driverId"),
                "driverName": v.get("driverName"),
                "driverDallasKeyHexa": v.get("driverDallasKeyHexa"),
                "vehicleAttachments": v.get("vehicleAttachments"),
                "vehicleCategoryId": category_id,
                "vehicleCategoryReference": category_reference,
                "vehicleCategoryName": category_name,
                "vehicleCategoryIcon": category_icon,
                "vehicleCategoryDefault": category_default,
                "vehicleIsACopy": v.get("vehicleIsACopy"),
                "startingDateTimestamp": v.get("startingDateTimestamp"),
                "startingDateAsLocalDateTime": v.get("startingDateAsLocalDateTime"),
                "startingDateTime": v.get("startingDateTime"),
                "startingDate": v.get("startingDate"),
                "startingTime": v.get("startingTime"),
                "startingLongitude": v.get("startingLongitude"),
                "startingLatitude": v.get("startingLatitude"),
                "startingAddress": v.get("startingAddress"),
                "startingAddressCountry": v.get("startingAddressCountry"),
                "startingAddressCity": v.get("startingAddressCity"),
                "startingAddressPostCode": v.get("startingAddressPostCode"),
                "startingAddressRegion": v.get("startingAddressRegion"),
                "startingAddressStreet": v.get("startingAddressStreet"),
                "startingAddressStreetNumber": v.get("startingAddressStreetNumber"),
                "startingGeozoneNames": v.get("startingGeozoneNames"),
                "startingGeozoneNamesAndAddress": v.get(
                    "startingGeozoneNamesAndAddress"
                ),
                "startingGeozoneReferences": v.get("startingGeozoneReferences"),
                "startingGeozoneReferencesAsList": v.get(
                    "startingGeozoneReferencesAsList"
                ),
                "startingGeozoneIds": v.get("startingGeozoneIds"),
                "startingGeozones": v.get("startingGeozones"),
                "startingGeozoneColorsCommaSeparated": v.get(
                    "startingGeozoneColorsCommaSeparated"
                ),
                "endingDateTimestamp": v.get("endingDateTimestamp"),
                "endingDateTime": v.get("endingDateTime"),
                "endingDate": v.get("endingDate"),
                "endingTime": v.get("endingTime"),
                "endingLongitude": v.get("endingLongitude"),
                "endingLatitude": v.get("endingLatitude"),
                "endingAddress": v.get("endingAddress"),
                "endingAddressCountry": v.get("endingAddressCountry"),
                "endingAddressCity": v.get("endingAddressCity"),
                "endingAddressPostCode": v.get("endingAddressPostCode"),
                "endingAddressRegion": v.get("endingAddressRegion"),
                "endingAddressPostCode": v.get("endingAddressPostCode"),
                "endingAddressStreet": v.get("endingAddressStreet"),
                "endingAddressStreetNumber": v.get("endingAddressStreetNumber"),
                "endingGeozoneName": v.get("endingGeozoneName"),
                "endingGeozoneNameAndAddress": v.get("endingGeozoneNameAndAddress"),
                "endingGeozoneReferences": v.get("endingGeozoneReferences"),
                "endingGeozoneReferencesAsList": v.get("endingGeozoneReferencesAsList"),
                "endingGeozoneIds": v.get("endingGeozoneIds"),
                "endingGeozones": v.get("endingGeozones"),
                "endingGeozoneColorsCommaSeparated": v.get(
                    "endingGeozoneColorsCommaSeparated"
                ),
                "mediumSpeed": v.get("mediumSpeed"),
                "stoppedDurationUntilNextTripSeconds": v.get(
                    "stoppedDurationUntilNextTripSeconds"
                ),
                "idlingDurationSeconds": v.get("idlingDurationSeconds"),
                "drivingDurationSeconds": v.get("drivingDurationSeconds"),
                "tripDurationSeconds": v.get("tripDurationSeconds"),
                "tripDistanceOnDistanceUnit": v.get("tripDistanceOnDistanceUnit"),
                "tripFuelOnFuelUnit": v.get("tripFuelOnFuelUnit"),
                "weekNumber": v.get("weekNumber"),
                "workerIds": v.get("workerIds"),
                "workerNames": v.get("workerNames"),
                "mobileAssetIds": v.get("mobileAssetIds"),
                "mobileAssetNames": v.get("mobileAssetNames"),
                "privateTrip": v.get("privateTrip"),
                "distanceError": v.get("distanceError"),
                "fuelError": v.get("fuelError"),
                "startBecausePrivateStop": v.get("startBecausePrivateStop"),
                "stopBecausePrivateStart": v.get("stopBecausePrivateStart"),
                "temperatureTags": v.get("temperatureTags"),
                "trackingObjects": v.get("trackingObjects"),
                "equipments": v.get("equipments"),
                "equipment1": v.get("equipment1"),
                "equipment2": v.get("equipment2"),
                "equipment3": v.get("equipment3"),
                "equipment4": v.get("equipment4"),
                "endingVehicleOdometerInKm": v.get("endingVehicleOdometerInKm"),
                "idleTrip": v.get("idleTrip"),
            }
        )

    return pd.DataFrame(reports_array)


def sort_trips(trips_json):

    trips_array = []
    for v in trips_json:

        # nested dictonnaries
        asset = v.get("asset")
        asset_id = asset.get("id") if asset else None
        asset_reference = asset.get("reference") if asset else None
        asset_name = asset.get("name") if asset else None

        startingAddress = v.get("startingAddress")
        startingAddressHouseNumber = (
            startingAddress.get("houseNumber") if startingAddress else None
        )
        startingAddressStreet = (
            startingAddress.get("street") if startingAddress else None
        )
        startingAddressLine2 = startingAddress.get("line2") if startingAddress else None
        startingAddressPostCode = (
            startingAddress.get("postCode") if startingAddress else None
        )
        startingAddressCity = startingAddress.get("city") if startingAddress else None
        startingAddressRegion = (
            startingAddress.get("region") if startingAddress else None
        )
        startingAddressCounty = (
            startingAddress.get("county") if startingAddress else None
        )
        startingAddressState = startingAddress.get("state") if startingAddress else None
        startingAddressCountry = (
            startingAddress.get("country") if startingAddress else None
        )
        startingAddressFormattedAddress = (
            startingAddress.get("formattedAddress") if startingAddress else None
        )

        endingAddress = v.get("endingAddress")
        endingAddressHouseNumber = (
            endingAddress.get("houseNumber") if endingAddress else None
        )
        endingAddressStreet = endingAddress.get("street") if endingAddress else None
        endingAddressLine2 = endingAddress.get("line2") if endingAddress else None
        endingAddressPostCode = endingAddress.get("postCode") if endingAddress else None
        endingAddressCity = endingAddress.get("city") if endingAddress else None
        endingAddressRegion = endingAddress.get("region") if endingAddress else None
        endingAddressCounty = endingAddress.get("county") if endingAddress else None
        endingAddressState = endingAddress.get("state") if endingAddress else None
        endingAddressCountry = endingAddress.get("country") if endingAddress else None
        endingAddressFormattedAddress = (
            endingAddress.get("formattedAddress") if endingAddress else None
        )

        trips_array.append(
            {
                "id": v.get("id"),
                "asset_id": asset_id,
                "asset_reference": asset_reference,
                "asset_name": asset_name,
                "distance": v.get("distance") / 1000,  # in km
                "alreadyQualified": v.get("alreadyQualified"),
                "startingDate": v.get("startingDate"),
                "startingGeozone": v.get("startingGeozone"),
                "startingAddressHouseNumber": startingAddressHouseNumber,
                "startingAddressStreet": startingAddressStreet,
                "startingAddressLine2": startingAddressLine2,
                "startingAddressPostCode": startingAddressPostCode,
                "startingAddressCity": startingAddressCity,
                "startingAddressRegion": startingAddressRegion,
                "startingAddressCounty": startingAddressCounty,
                "startingAddressState": startingAddressState,
                "startingAddressCountry": startingAddressCountry,
                "startingAddressFormattedAddress": startingAddressFormattedAddress,
                "endingDate": v.get("endingDate"),
                "endingGeozone": v.get("endingGeozone"),
                "endingAddressHouseNumber": endingAddressHouseNumber,
                "endingAddressStreet": endingAddressStreet,
                "endingAddressLine2": endingAddressLine2,
                "endingAddressPostCode": endingAddressPostCode,
                "endingAddressCity": endingAddressCity,
                "endingAddressRegion": endingAddressRegion,
                "endingAddressCounty": endingAddressCounty,
                "endingAddressState": endingAddressState,
                "endingAddressCountry": endingAddressCountry,
                "endingAddressFormattedAddress": endingAddressFormattedAddress,
            }
        )

    return pd.DataFrame(trips_array)


# Colonne CO2-Facteur WTT -> vehicles_df


def column_co2_facteur_wtt(row):

    if row["vehicleCategoryName"] == "Véhicule électrique":
        return 0.026
    elif row["vehicleCategoryName"] == "Grande voiture":
        return 0.058
    elif row["vehicleCategoryName"] == "Voiture moyenne":
        return 0.045
    elif row["vehicleCategoryName"] == "Van (jusqu'à 3.5T)":
        return 0.059
    elif row["vehicleCategoryName"] == "Grand camion (jusqu'à 40T)":
        return 0.221
    elif row["vehicleCategoryName"] == "Camion moyen (jusqu'à 17T)":
        return 0.142
    elif row["vehicleCategoryName"] == "Petit camion (jusqu'à 7.5T)":
        return 0.117
    else:
        return 0.039


# -> puis faire Distance_en_km * ce_Facteur

# "Masse carburant"


def column_masse_carburant(row):

    if row["engineType"] == "ELECTRIC":
        return 0.026
    elif row["engineType"] == "DIESEL":
        return 3.33
    elif row["engineType"] == "GASOLINE":
        return 2.94
    elif row["engineType"] == "GAS":
        return 2.75
    elif row["engineType"] == "HYBRID":
        return 3 * 0.8
    else:
        return 0

        # -> puis faire "CO2-eq Kg" / ce_facteur


# "Unité Carburant"
# Carburants : DIESEL (L), ELECTRIC (kMh), GAS  (Kg), GASOLINE (L), HYBRID (L)


def column_unite_carburant(row):

    if row["engineType"] == "ELECTRIC":
        return "kWh"
    elif row["engineType"] == "DIESEL":
        return "Litre"
    elif row["engineType"] == "GASOLINE":
        return "Litre"
    elif row["engineType"] == "GAS":
        return "Kilogramme"
    elif row["engineType"] == "HYBRID":
        return "Litre"
    else:
        return "Inconnu"


def calcul_co2_direct(row):
    # CO2-Direct

    dist_km = row["distance"]

    if row["vehicleCategoryName"] == "Véhicule électrique":
        return dist_km * 0
    elif row["vehicleCategoryName"] == "Grande voiture":
        return dist_km * 0.226
    elif row["vehicleCategoryName"] == "Voiture moyenne":
        return dist_km * 0.171
    elif row["vehicleCategoryName"] == "Van (jusqu'à 3.5T)":
        return dist_km * 0.240
    elif row["vehicleCategoryName"] == "Grand camion (jusqu'à 40T)":
        return dist_km * 0.916
    elif row["vehicleCategoryName"] == "Camion moyen (jusqu'à 17T)":
        return dist_km * 0.587
    elif row["vehicleCategoryName"] == "Petit camion (jusqu'à 7.5T)":
        return dist_km * 0.481
    else:
        return dist_km * 0.145


def calcul_co2_eq_kg(row):
    # "CO2-eq Kg"

    return row["co2_direct"] + row["co2_facteur_wtt"]


def split_into_monthly_ranges(start_date_str, end_date_str):

    start = datetime.strptime(start_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    end = datetime.strptime(end_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")

    result = []
    current = start

    while current < end:
        next_month = current + relativedelta(months=1)
        chunk_end = min(next_month, end)
        result.append(
            {
                "start": current.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
                "end": chunk_end.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
            }
        )
        current = chunk_end

    return result


def extract_year_month_number(row):
    date_str = row["startingDate"].split("T")[0]
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.month


def extract_year_month_name(row):
    date_str = row["startingDate"].split("T")[0]
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    month_name = dt.strftime("%B")  # Nom complet du mois
    return "%s %d" % (month_name, dt.year)
