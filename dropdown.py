from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/dropdown")
print("Opened dropdown page")

dropdown_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "dropdown"))
)

dropdown = Select(dropdown_element)

dropdown.select_by_visible_text("Option 1")
print("Selected by text:", dropdown.first_selected_option.text)
time.sleep(2)

dropdown.select_by_value("2")
print("Selected by value:", dropdown.first_selected_option.text)
time.sleep(2)

dropdown.select_by_index(1)
print("Selected by index:", dropdown.first_selected_option.text)
time.sleep(2)

time.sleep(10)
driver.quit()
print("Done")