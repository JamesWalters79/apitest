
import pytest
import datetime

from make_requests import make_request_feed

class TestClass:
    def test_search_asteroids_with_sucess(self):
        # Arrange:
        query_parameters = "api_key=4oHMkn6CWYCvBFcX5GWusj5pNGgLFTY1LiWgg2n5"
        # Act:
        response = make_request_feed(query_parameters)
        # Assertion:
        assert response.status_code == 200  # Validation of status code
        data = response.json()
        # Assertion of body response content:
        assert len(data) > 0
        assert data["element_count"] > 0

    def test_search_asteroids_with_query_parameters_empty(self):
        # Arrange:
        query_parameters = ""
        # Act:
        response = make_request_feed(query_parameters)
        # Assertion:
        assert response.status_code == 403

    def test_search_asteroids_with_start_date(self):
        # Arrange:
        query_parameters = "api_key=4oHMkn6CWYCvBFcX5GWusj5pNGgLFTY1LiWgg2n5&start_date=2023-11-10"
        # Act:
        response = make_request_feed(query_parameters)
        # Assertion:
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        assert data["element_count"] > 0

    def test_search_asteroids_with_end_date(self):
        # Arrange:
        query_parameters = "api_key=4oHMkn6CWYCvBFcX5GWusj5pNGgLFTY1LiWgg2n5&end_date=2023-11-10"
        # Act:
        response = make_request_feed(query_parameters)
        # Assertion:
        assert response.status_code == 400

    def test_search_asteroids_in_valid_range(self):
        # Arrange:
        query_parameters = "api_key=4oHMkn6CWYCvBFcX5GWusj5pNGgLFTY1LiWgg2n5&start_date=2023-11-09&end_date=2023-11-10"
        # Act:
        response = make_request_feed(query_parameters)
        # Assertion:
        assert response.status_code == 200

    def test_search_asteroids_in_invalid_range(self):
        # Arrange:
        query_parameters = "api_key=4oHMkn6CWYCvBFcX5GWusj5pNGgLFTY1LiWgg2n5&start_date=2023-11-19&end_date=2023-11-10"
        # Act:
        response = make_request_feed(query_parameters)
        # Assertion:
        assert response.status_code == 400

    def test_search_asteroids_in_invalid_token(self):
        # Arrange:
        query_parameters = "api_key=INVALID_TOKEN"
        # Act:
        response = make_request_feed(query_parameters)
        # Assertion:
        assert response.status_code == 403