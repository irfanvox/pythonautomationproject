import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    
    yield driver

    # Screenshot folder
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    # Save screenshot irrespective of pass/fail
    test_name = request.node.name
    screenshot_path = f"screenshots/{test_name}.png"
    driver.save_screenshot(screenshot_path)

    driver.quit()
