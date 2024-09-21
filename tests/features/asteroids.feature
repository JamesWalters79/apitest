Feature: Asteroids Search

@bdd @neo_feed
Scenario: Asteroids API Query with no search parameters
    Given the Asteroids API is queried with no search parameters
    Then the response status code is "200"
    And many asteroids are returned
    And the element count is between "100" and "150"

@bdd @neo_feed
Scenario: Asteroids API Query with start date
    Given the Asteroids API is queried with start date "2023-11-10"
    Then the response status code is "200"
    And many asteroids are returned
    And the element count is between "150" and "200"

@bdd @neo_feed
Scenario: Asteroids API Query with end date
    Given the Asteroids API is queried with end date "2023-11-10"
    Then the response status code is "400"
    And the http error is "BAD_REQUEST"
    And the http error message is "Date Format Exception - Expected format (yyyy-mm-dd) - The Feed date limit is only 7 Days"

@bdd @neo_feed
Scenario: Asteroids API Query with valid range
    Given the Asteroids API is queried with start date "2023-11-09" and end date "2023-11-10"
    Then the response status code is "200"
    And many asteroids are returned
    And the element count is between "30" and "50"

@bdd @neo_feed
Scenario: Asteroids API Query with invalid range
    Given the Asteroids API is queried with start date "2023-11-09" and end date "2023-12-10"
    Then the response status code is "400"
    And the http error is "BAD_REQUEST"
    And the http error message is "Date Format Exception - Expected format (yyyy-mm-dd) - The Feed date limit is only 7 Days"

@bdd @neo_core
Scenario: Asteroids API Query with invalid token
    Given the Asteroids API is queried with an invalid token
    Then the response status code is "403"
    And the error code is "API_KEY_INVALID"
    And the error message is "An invalid api_key was supplied. Get one at https://api.nasa.gov:443"

@bdd @neo_browse
Scenario: Asteroids API browse
    Given the Asteroids API is browsed
    Then the response status code is "200"

@bdd @neo_lookup
Scenario: Asteroids API lookup by ID
    Given the Asteroids API is asked for an asteroid with id "3542519"
    Then the response status code is "200"