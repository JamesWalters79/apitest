import requests

def make_request_feed(query_parameters):
    base_url = "https://api.nasa.gov/neo/rest/v1/feed"
    response = requests.get(f'{base_url}?{query_parameters}')
    return response

def make_request_browse(query_parameters):
    base_url = "https://api.nasa.gov/neo/rest/v1/neo/browse"
    response = requests.get(f'{base_url}?{query_parameters}')
    return response

def make_request_lookup(lookup_id,query_parameters):
    base_url = "https://api.nasa.gov/neo/rest/v1/neo/"
    response = requests.get(f'{base_url}{lookup_id}?{query_parameters}')
    return response