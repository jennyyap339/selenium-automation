from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/iframe")
print("Opened iframe page")

# Wait for the iframe to appear
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr"))
    )
print("Switched to iframe")

# Now we can interact with elements inside the iframe
text_area = driver.find_element(By.ID, "tinymce")
print("Found text area inside iframe")
print("Current text:", text_area.text)

# Clear existing text and type new text
# Instead of text_area.clear() and text_area.send_keys()
# Use JavaScript to clear and type into the rich text editor
driver.execute_script("arguments[0].innerHTML = '';", text_area)
print("Cleared text area")
driver.execute_script("arguments[0].innerHTML = 'Hello from inside an iframe';", text_area)
print("Typed into iframe")

time.sleep(3)

# Switch BACK to the main page
driver.switch_to.default_content()
print("Switched back to main page")

# Now we can interact with main page elements again
print("Page title:", driver.title)

time.sleep(2)
driver.quit()
print("Done")