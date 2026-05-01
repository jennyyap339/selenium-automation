import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from pages.login_page import LoginPage
from tests.helpers import read_csv_data, read_json_data, read_excel_data

# Test with CSV data
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("username, password, expected, should_pass", read_csv_data())
def test_login_csv(driver, username, password, expected, should_pass):
    login = LoginPage(driver)
    login.open()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    if should_pass:
        message = login.get_success_message()
        assert expected in message, f"Expected '{expected}' in success message"
        print(f"CSV: Login passed for {username}")
    else:
        try:
            message = login.get_error_message()
            assert expected in message, f"Expected '{expected}' in error message"
            print(f"CSV: Failed login correct for {username}")
        except:
            assert False, f"No error message found for {username}"

# Test with JSON data
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("username, password, expected, should_pass", read_json_data())
def test_login_json(driver, username, password, expected, should_pass):
    login = LoginPage(driver)
    login.open()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    if should_pass:
        message = login.get_success_message()
        assert expected in message, f"Expected '{expected}' in success message"
        print(f"JSON: Login passed for {username}")
    else:
        try:
            message = login.get_error_message()
            assert expected in message, f"Expected '{expected}' in error message"
            print(f"JSON: Failed login correct for {username}")
        except:
            assert False, f"No error message found for {username}"

# Test with Excel data
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("username, password, expected, should_pass", read_excel_data())
def test_login_excel(driver, username, password, expected, should_pass):
    login = LoginPage(driver)
    login.open()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    if should_pass:
        message = login.get_success_message()
        assert expected in message, f"Expected '{expected}' in success message"
        print(f"Excel: Login passed for {username}")
    else:
        try:
            message = login.get_error_message()
            assert expected in message, f"Expected '{expected}' in error message"
            print(f"Excel: Failed login correct for {username}")
        except:
            assert False, f"No error message found for {username}"

@pytest.mark.regression
@pytest.mark.login
def test_login_page_title(driver):
    login = LoginPage(driver)
    login.open()
    assert "Internet" in driver.title
    print("Login page title correct")

@pytest.mark.regression
def test_login_url(driver):
    login = LoginPage(driver)
    login.open()
    assert "login" in driver.current_url
    print("Login URL correct")