from playwright.sync_api import Playwright, sync_playwright

def test_login_form(playwright: Playwright):
    # Launch the browser and create a new page
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Navigate to the login page
    page.goto("https://example.com/login")

    # Fill in the username and password fields
    username_field = page.locator("#username")
    password_field = page.locator("#password")
    username_field.fill("myusername")
    password_field.fill("mypassword")

    # Click the submit button and wait for the page to load
    submit_button = page.locator("#submit")
    submit_button.click()
    page.wait_for_selector("#dashboard")

    # Assert that the user has successfully logged in
    assert page.title() == "Dashboard - Example.com"

    # Close the browser
    browser.close()
