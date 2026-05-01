from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # URL of the page
    URL = "https://the-internet.herokuapp.com/login"

    # Element locators
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON   = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG    = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MSG      = (By.CSS_SELECTOR, ".flash.error")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.USERNAME_FIELD)
        )
        field.send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MSG)
        ).text

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text
    
    def take_screenshot(self, filename):
        path = f"screenshots/{filename}"
        self.driver.save_screenshot(path)
        print(f"Screenshot saved as {path}")