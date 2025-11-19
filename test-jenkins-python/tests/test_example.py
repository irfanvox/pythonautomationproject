import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

REPORTS_DIR = "/app/reports"
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Headless for automation
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    # take screenshot on success
    driver.save_screenshot(os.path.join(SCREENSHOTS_DIR, "google_search.png"))
