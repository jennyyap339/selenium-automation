from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/checkboxes")
print("Opened checkboxes page")

# Get all checkboxes on the page
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print("Found", len(checkboxes), "checkboxes") # Found ? checkboxes

# Check the state of each one
for i, checkbox in enumerate(checkboxes):
    print(f"Checkbox {i+1} checked: {checkbox.is_selected()}") # Checkbox ? checked: False or True

# Click checkbox 1 to toggle it
time.sleep(2)
checkboxes[0].click()
print("Clicked checkbox 1")

# Untick checkbox if it's already checked
if checkboxes[1].is_selected():
    time.sleep(2)
    checkboxes[1].click()
    print("Unticked checkbox 2")
else:
    print("Checkbox 2 was already unticked")

time.sleep(3)
driver.quit()
print("Done!")