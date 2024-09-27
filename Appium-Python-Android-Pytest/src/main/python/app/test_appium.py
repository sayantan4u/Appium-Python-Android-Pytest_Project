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
    allure.dynamic.title("Test Android Emulator - Horizontal Swipe")
    allure.dynamic.description(
        "This test attempts to open WDIODEMOAPP in Android Emulator and horizotal swipe function.\n\nNote that this test does not test Authentication.")
    allure.dynamic.tag("NewUI", "Essentials", "Authentication")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "Sayantan Dutta")
    allure.dynamic.link("https://github.com/webdriverio/native-demo-app/releases", name="Website")
    allure.dynamic.issue("AEHS-123")
    allure.dynamic.testcase("TMS-456")
    allure.dynamic.epic("Emulator Testing")
    allure.dynamic.feature("Swipe features")
    allure.dynamic.story("Swipe Horizontal carousel actions")
    allure.dynamic.parent_suite("Tests Suite forAndroid Emulators")
    allure.dynamic.suite("Tests for Swipe feature")
    allure.dynamic.sub_suite("Tests for Swipe Horizontal carousel actions")
    driver = appium_driver_setup_teardown
    print('Testing WDIODemoApp Swipe function')
    with allure.step("Step 1: Testing WDIODemoApp Swipe function"):
        wait_in_seconds = 20
        # Implicit wait
        driver.implicitly_wait(wait_in_seconds)
        # Click on the 'Swipe' tab from down menu
    with allure.step("Step 2: Click WDIODemoApp Swipe tab"):
        el1 = driver.find_element(
            by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Swipe']")
        el1.click()
    # Explicit wait and then Swipe left (can use - EC.element_to_be_clickable)
    with allure.step("Step 3: Click Carousel Swipe horizontally"):
        carousel = WebDriverWait(driver, wait_in_seconds).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Carousel")))
        driver.execute_script("gesture: swipe", {
            "elementId": carousel.id,
            "percentage": 50,
            "direction": "left"
        })

