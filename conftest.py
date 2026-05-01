import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup Chrome options
    options = Options()
    options.add_argument("--headless")           # no screen on server
    options.add_argument("--no-sandbox")         # required for Linux
    options.add_argument("--disable-dev-shm-usage") # required for Linux
    options.add_argument("--incognito")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordCheck")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    # Create driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)

    yield driver  # hand driver to the test

    # Cleanup — runs after every test automatically
    driver.quit()