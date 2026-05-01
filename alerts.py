from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
print("Opened alerts page")

# --- Alert (just OK button) ---
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print("Alert text:", alert.text)
time.sleep(2)
alert.accept()
print("Accepted Alert")

time.sleep(2)

# --- Confirm (OK and Cancel buttons) ---
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
confirm = driver.switch_to.alert
print("Confirm text:", confirm.text)
time.sleep(2)
confirm.dismiss()
print("Dismissed confirm")

time.sleep(2)

# --- Prompt (OK, Cancel and a text input) ---
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
prompt = driver.switch_to.alert
print("Prompt text:", prompt.text)
prompt.send_keys("Hello from Selenium")
time.sleep(3)
prompt.accept()
print("Typed and accepted prompt")

# Read the result message on the page
result = driver.find_element(By.ID, "result")
print("Result:", result.text)

time.sleep(3)
driver.quit()
print("Done")