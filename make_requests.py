import requests

#Constants
BASE_URL = "https://api.nasa.gov/neo/rest/v1/"

def make_request_feed(query_parameters):
    response = requests.get(f'{BASE_URL}feed?{query_parameters}')
    return response

def make_request_browse(query_parameters):
    response = requests.get(f'{BASE_URL}neo/browse?{query_parameters}')
    return response

def make_request_lookup(lookup_id,query_parameters):
    response = requests.get(f'{BASE_URL}neo/{lookup_id}?{query_parameters}')
    return response