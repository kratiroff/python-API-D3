import requests

def get_anything():
    anything = requests.get("http://httpbin.org/anything")
    return anything.json()
