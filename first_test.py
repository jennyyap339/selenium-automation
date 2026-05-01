from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)

# Go to Google
driver.get("https://the-internet.herokuapp.com/login")
print("Opened Login page")

# Wait until the search box is ready to be typed into
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "username"))
    )
print("Login form is ready")

username.send_keys("tomsmith")
password = driver.find_element(By.ID, "password")
password.send_keys("WrongPassword!")
print("Filled in credentials")

# Click the login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
print("Clicked login")

# Wait until success message appears
try:
    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
    print("Login successful")
    print("Message:", success.text)
except:
    error = driver.find_element(By.CSS_SELECTOR, ".flash.error")
    print("Login Failed")
    print("Message:", error.text)

time.sleep(3)
driver.quit()
print("Done!")