import pytest
import allure
from pytest import StashKey, CollectReport

from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from typing import Any, Dict
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

phase_report_key = StashKey[Dict[str, CollectReport]]()
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # set a report attribute for each phase of a call, which can
#     # be "setup", "call", "teardown"
#     setattr(item, "rep_" + rep.when, rep)
#     return rep


@pytest.hookimpl(wrapper=True, tryfirst=True)
@allure.title("Prepare for the tests")
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    rep = yield

    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep

    return rep


@pytest.fixture(scope='function')
def appium_driver_setup_teardown():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()
    global driver
    print('Running in Setup function')
    options = AppiumOptions()
    # Local Emulator Capability
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "appium:udid": "emulator-5554", # it can be "emulator-5554" check using 'adb devices' which one is online
        "appium:appPackage": "com.wdiodemoapp",
        "appium:appActivity": "com.wdiodemoapp.MainActivity",
        #	"appium:app": "/Users/sayantan/Downloads/android.wdio.native.app.v1.0.8.apk",
        "appium:deviceName": "Pixel7-API-31",
        "appium:automationName": "UiAutomator2",
        "appium:platformVersion": "12",
        "appium:autoGrantPermissions": True,
        "appium:appWaitForLaunch": False,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 8000,
        "appium:connectHardwareKeyboard": True
    }
    options.load_capabilities(cap)
    url = 'http://127.0.0.1:4723'

    # Connect to the appium server instance with above desired capabilities
    driver = webdriver.Remote(url, options=options)
    yield driver
    driver.quit()

# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def adding_screenshot_Fail(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope

    # if hasattr(request.node, 'rep_call' and request.node.rep_call.failed):
    #     try:
    #         allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,
    #                       attachment_type=AttachmentType.PNG)
    #     except:
    #         pass
    report = request.node.stash[phase_report_key]
    if report["setup"].failed:
        print("setting up a test failed or skipped", request.node.nodeid)
    elif report["setup"].passed:
        if ("call" not in report) or report["call"].failed:
            allure.attach(driver.get_screenshot_as_png(),name=request.function.__name__, attachment_type=allure.attachment_type.PNG)
            print("executing test failed or skipped", request.node.nodeid)