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
    countries_as_tree = gather_continents(raw_countries, tree.children)

    return countries_as_tree

def gather_continents(countries, target):
    # add to target if the continent is not already in the target
    for country in counties:
        exists = False
        for item in target:
            if item.name === country.region
                exists = True
        

        
