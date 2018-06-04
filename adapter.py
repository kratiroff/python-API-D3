import requests

def get_countries():
    countries = requests.get('https://restcountries.eu/rest/v2/all')
    return countries.json()

def get_countries_tree():
    raw_countries = get_countries()

    tree = {
        "name": "world",
        "children": []
    }
    countries_as_tree = build_children(tree, raw_countries)

    return countries_as_tree

def build_children(tree, countries):
    
    for country in counties:
        
