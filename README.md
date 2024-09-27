# Appium-Python-Android-Pytest_Project
This is a Test Automation project for Android app 'wdiodemo'.

### **The tools and frameworks used:**

1. Appium - 2.11.3
2. Python - 3.12.6
3. PyCharm CE - 2024.2.3
4. In PyCharm CE you need to install the following packages/ plugins latest versions:
    a. Appium-Python-Client (4.2.0)
    b. pytest (8.3.3)
    c. allure-pytest (2.13.5)
5. Android Studio - Koala - 2024.1.1
6. Emulator used: Pixel7_API_31 ("appium:udid": "emulator-5554", this might change for you. use 'adb devices' to check after starting the Emulator)

### **How to Execute**
1. In one terminal start emulator:
    _$ANDROID_HOME/emulator/emulator @Pixel7_API_31_
2. In another terminal tab, start appium:
    _appium --address 127.0.0.1 --port 4723 --use-plugins gestures_
3. Now open PyCharm CE and open the project.
4. In Terminal ensure you activated python virtual environment (_python3 -m venv .venv_ AND _source .venv/bin/activate_)
5. Execute : _pytest -v -s Appium-Python-Android-Pytest/src/main/python/app/test_appium.py --alluredir="./allureReport/"_
6. To check the report: _allure serve ./allureReport_
