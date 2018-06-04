import requests

def get_countries():
    countries = requests.get('https://restcountries.eu/rest/v2/all')
    return countries.json()

def get_countries_tree():
    raw_countries = get_countries()
    # TODO
    return raw_countries
