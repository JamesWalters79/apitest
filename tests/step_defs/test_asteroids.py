import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers
from make_requests import make_request_feed
from make_requests import make_request_browse
from make_requests import make_request_lookup

# Constants
ASTEROIDS_API_KEY = "4oHMkn6CWYCvBFcX5GWusj5pNGgLFTY1LiWgg2n5"
INVALID_ASTEROIDS_API_KEY = "1234"

# Load all scenarios from the asteroids feature file
scenarios("../features/asteroids.feature")

# Given Steps
@given(parsers.parse('the Asteroids API is asked for an asteroid with id "{asteroid_id}"'), target_fixture='asteroids_response')
def asteroids_response(asteroid_id):
    response = make_request_lookup(asteroid_id,f'api_key={ASTEROIDS_API_KEY}')
    return response

@given("the Asteroids API is browsed", target_fixture='asteroids_response')
def asteroids_response():
    response = make_request_browse(f'api_key={ASTEROIDS_API_KEY}')
    return response

@given("the Asteroids API is queried with no search parameters", target_fixture='asteroids_response')
def asteroids_response():
    response = make_request_feed(f'api_key={ASTEROIDS_API_KEY}')
    return response

@given(parsers.parse('the Asteroids API is queried with start date "{start_date}"'), target_fixture='asteroids_response')
def asteroids_response_start_date(start_date):
    response = make_request_feed(f'api_key={ASTEROIDS_API_KEY}&start_date={start_date}')
    return response  

@given(parsers.parse('the Asteroids API is queried with end date "{end_date}"'), target_fixture='asteroids_response')
def asteroids_response_end_date(end_date):
    response = make_request_feed(f'api_key={ASTEROIDS_API_KEY}&end_date={end_date}')
    return response 

@given(parsers.parse('the Asteroids API is queried with start date "{start_date}" and end date "{end_date}"'), target_fixture='asteroids_response')
def asteroids_response_date_range(start_date, end_date):
    response = make_request_feed(f'api_key={ASTEROIDS_API_KEY}&start_date={start_date}&end_date={end_date}')
    return response 

@given("the Asteroids API is queried with an invalid token", target_fixture='asteroids_response')
def asteroids_response_invalid_token():
    response = make_request_feed(f'api_key={INVALID_ASTEROIDS_API_KEY}')
    return response

# Then Steps
@then(parsers.parse('the response status code is "{code:d}"'))
def asteroids_response_code_200(asteroids_response, code):
    assert asteroids_response.status_code == code

@then("many asteroids are returned")
def asteriods_response_count(asteroids_response):
    data = asteroids_response.json()
    assert len(data) > 0
    assert data["element_count"] > 0

@then(parsers.parse('the error code is "{code}"'))
def asteroids_response_error_code(asteroids_response, code):
    data = asteroids_response.json()
    assert data["error"]["code"] == code

@then(parsers.parse('the error message is "{message}"'))
def asteroids_response_error_message(asteroids_response, message):
    data = asteroids_response.json()
    assert data["error"]["message"] == message

@then(parsers.parse('the http error message is "{http_error_message}"'))
def asteroids_response_http_error_message(asteroids_response, http_error_message):
    data = asteroids_response.json()
    assert data["error_message"] == http_error_message

@then(parsers.parse('the http error is "{http_error}"'))
def asteroids_response_http_error(asteroids_response, http_error):
    data = asteroids_response.json()
    assert data["http_error"] == http_error

@then(parsers.parse('the element count is between "{element_count_lower:n}" and "{element_count_upper:n}"'))
def asteroids_response_element_count(asteroids_response, element_count_lower, element_count_upper):
    data = asteroids_response.json()
    assert data["element_count"] > element_count_lower
    assert data["element_count"] < element_count_upper