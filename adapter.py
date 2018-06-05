import requests

def get_countries():
    countries = requests.get('https://restcountries.eu/rest/v2/all')
    return countries.json()

def get_countries_tree():
    raw_countries = get_countries()

    continents = gather_continents(raw_countries, [])
    regions = gather_regions(raw_countries, continents)
    full_tree = gather_countries(raw_countries, continents, regions)

    return full_tree

def gather_continents(countries, target):
    # add to target if the continent is not already in the target
    for country in countries:
        exists = False
        for item in target:
            if item == country["region"]:
                exists = True
        if not exists:
            target.append(country["region"])

    # transform a list of names into a list of objects that have a name and a children property    
    target = map(lambda x: { 'name': x, 'children': [] }, target)

    return target

def gather_regions(countries, continents):
    regions = []
    # print continents
    for continent in continents:
        # 1. gather countries per region
        detailed_list = filter(lambda x: x["region"] == continent["name"], countries)
        # 2. only keep the subregion
        subregion_list = list(map(lambda x: x["subregion"], detailed_list))
        # 3. remove duplicates
        uniq_list = list(set(subregion_list))
        # 4. add children array
        with_empty_children = map(lambda x: { "name": x, "children": [] } , uniq_list)
        # 5. append to the list
        regions.append({ "name": continent["name"], "children": with_empty_children })
    return regions

def gather_countries(countries, continents, regions):
    tree = {
        "name": "world",
        "children": []
    }

    for region in regions:
        for child in region["children"]:
            detailed_list = filter(lambda x: x["subregion"] == child["name"], countries)
            countries_list = list(map(lambda x: x["name"], detailed_list))
            uniq_list = list(set(countries_list))
            child["children"] = uniq_list
        tree["children"].append(region)

    return tree
