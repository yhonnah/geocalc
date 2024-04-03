def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "inches_to_cm": 2.54,
        "feet_to_meters": 0.3048,
        "yards_to_meters": 0.9144,
        "miles_to_km": 1.60934,
        "cm_to_inches": 1 / 2.54,
        "meters_to_feet": 1 / 0.3048,
        "meters_to_yards": 1 / 0.9144,
        "km_to_miles": 1 / 1.60934
    }

    if from_unit == "inches":
        value_meters = value * conversion_factors["inches_to_cm"] / 100
    elif from_unit == "feet":
        value_meters = value * conversion_factors["feet_to_meters"]
    elif from_unit == "yards":
        value_meters = value * conversion_factors["yards_to_meters"]
    elif from_unit == "miles":
        value_meters = value * conversion_factors["miles_to_km"] * 1000
    elif from_unit == "cm":
        value_meters = value / 100
    elif from_unit == "meters":
        value_meters = value
    elif from_unit == "km":
        value_meters = value * 1000

    if to_unit == "inches":
        result = value_meters / conversion_factors["cm_to_inches"] * 100
    elif to_unit == "feet":
        result = value_meters / conversion_factors["meters_to_feet"]
    elif to_unit == "yards":
        result = value_meters / conversion_factors["meters_to_yards"]
    elif to_unit == "miles":
        result = value_meters / 1000 / conversion_factors["km_to_miles"]
    elif to_unit == "cm":
        result = value_meters * 100
    elif to_unit == "meters":
        result = value_meters
    elif to_unit == "km":
        result = value_meters / 1000

    return result