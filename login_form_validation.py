from playwright.sync_api import Playwright, sync_playwright

def test_login_form_inputs(playwright: Playwright):
    # Launch the browser and create a new page
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Navigate to the login page
    page.goto("https://example.com/login")

    # Test invalid username inputs
    username_field = page.locator("#username")
    username_field.fill("")
    error_message = page.locator("#username-error")
    assert error_message.is_visible()
    username_field.fill("short")
    assert error_message.is_visible()

    # Test invalid password inputs
    password_field = page.locator("#password")
    password_field.fill("")
    error_message = page.locator("#password-error")
    assert error_message.is_visible()
    password_field.fill("weak")
    assert error_message.is_visible()

    # Test valid inputs
    username_field.fill("myusername")
    password_field.fill("mypassword")
    submit_button = page.locator("#submit")
    submit_button.click()
    page.wait_for_selector("#dashboard")

    # Assert that the user has successfully logged in
    assert page.title() == "Dashboard - Example.com"

    # Close the browser
    browser.close()
