from playwright.sync_api import Playwright, sync_playwright
import requests

def test_api_login(playwright: Playwright):
    # Set the login endpoint and data
    login_url = "https://example.com/api/login"
    login_data = {"username": "myusername", "password": "mypassword"}

    # Send a POST request to the login API
    response = requests.post(login_url, data=login_data)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the API response contains the expected data
    expected_data = {"success": True, "token": "mytoken"}
    assert response.json() == expected_data
