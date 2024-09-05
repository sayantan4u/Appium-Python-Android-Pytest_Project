# appium service
import allure
import pytest

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from typing import Any, Dict
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("adding_screenshot_Fail")
def test_demo1(appium_driver_setup_teardown):
    driver = appium_driver_setup_teardown
    print('Testing WDIODemoApp function')
    wait_in_seconds = 10
    # Implicit wait
    driver.implicitly_wait(wait_in_seconds)
    # Click on the 'Swipe' tab from down menu
    el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Swipe']")
    el1.click()
    # Explicit wait and then Swipe left (can use - EC.element_to_be_clickable)
    carousel = WebDriverWait(driver, wait_in_seconds).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Carousel")))
    driver.execute_script("gesture: swipe", {
        "elementId": carousel.id,
        "percentage": 50,
        "direction": "left"
    })

