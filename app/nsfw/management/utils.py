# Configuration of Umweltbundesamt air data API entry points and API parameters
# https://www.umweltbundesamt.de/daten/luft/luftdaten/doc

UBA_BASE_URL = "https://www.umweltbundesamt.de/api/air_data/v2/measures/json?"

POLLUTANTS = { # https://www.umweltbundesamt.de/api/air_data/v2/components/json
    'PM10'  : '1', # Particulate matter
    'NO2'   : '5', # Nitrogen dioxide
}

SCOPES = { # https://www.umweltbundesamt.de/api/air_data/v2/scopes/json
    '1TMW'      : '1', # Daily average
    '1SMW_MAX'  : '3', # Maximum one hour average
}