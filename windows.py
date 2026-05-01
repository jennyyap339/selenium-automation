from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/windows")
print("Opened windows page")

# Store the original window handle
original_window = driver.current_window_handle
print("Original Window:", original_window)

# Click the link that opens a new window
driver.find_element(By.LINK_TEXT, "Click Here").click()
print("Clicked Link")

# Wait until a new window appears
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
print("New window opened")

# Get all open window handles
all_windows = driver.window_handles
print("Total windows open:", len(all_windows))

# Switch to the new window
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break
print("Switch to new window")
print("New window title:", driver.title)

time.sleep(2)

# Close the new window
driver.close()
print("Closed new window")

# Switch back to original window
driver.switch_to.window(original_window)
print("Switched back to original window")
print("Original window title:", driver.title)

time.sleep(2)
driver.quit()
print("Done")