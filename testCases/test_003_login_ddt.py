import os

import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.abspath(os.curdir) + "//testData//Opencart_LoginData.xlsx"


    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("**** Starting Data Driven Test Case for Login ****")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet 1')
        lst_status = []
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.logger.info(f"Current URL after load: {self.driver.current_url}")
        self.logger.info(f"Page Title after load: {self.driver.title}")

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2, self.rows + 1):
            self.logger.info(f"---------- Row {r} ----------")

            email = XLUtils.readData(self.path, "Sheet 1", r, 1)
            password = XLUtils.readData(self.path, "Sheet 1", r, 2)
            expected_result = XLUtils.readData(self.path, "Sheet 1", r, 3)

            if not email or not password or not expected_result:
                self.logger.warning(
                    f"Row {r} skipped due to missing data: email={email}, password={password}, expected={expected_result}")
                continue

            self.logger.info("Clicking on 'My Account'...")
            self.hp.clickMyAccount()
            time.sleep(2)  # Let dropdown/menu render

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Login"))
                )
                login_link = self.driver.find_element(By.LINK_TEXT, "Login")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", login_link)
                login_link.click()
                self.logger.info("Login link clicked successfully.")
            except Exception as e:
                self.logger.error(f"Failed to click 'Login' link: {e}")
                self.driver.save_screenshot(f"screenshots/login_link_failure_row{r}.png")
                lst_status.append("Fail")
                continue

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "input-email"))
                )
            except Exception as e:
                self.logger.error(f"Email input not visible for row {r}: {e}")
                self.driver.save_screenshot(f"screenshots/email_input_failure_row{r}.png")
                lst_status.append("Fail")
                continue

            self.logger.info(f"Testing with Email: {email}, Password: {password}, Expected: {expected_result}")

            self.lp.setEmail(email)
            self.lp.setPassword(password)
            self.lp.clickLogin()

            WebDriverWait(self.driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

            actual_result = self.lp.isMyAccountPageExists()

            if expected_result == "Valid":
                if actual_result:
                    self.logger.info("Login passed as expected (Valid)")
                    lst_status.append("Pass")
                    self.ma.clickLogout()
                else:
                    self.logger.error("Login failed unexpectedly (Valid)")
                    self.driver.save_screenshot(f"screenshots/failed_valid_login_row{r}.png")
                    lst_status.append("Fail")
            elif expected_result == "Invalid":
                if actual_result:
                    self.logger.error("Login passed unexpectedly (Invalid)")
                    self.driver.save_screenshot(f"screenshots/failed_invalid_login_row{r}.png")
                    self.ma.clickLogout()
                    lst_status.append("Fail")
                else:
                    self.logger.info("Login failed as expected (Invalid)")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("All data-driven login tests passed.")
            assert True
        else:
            self.logger.error("Some data-driven login tests failed.")
            assert False

        self.logger.info("******* End of test_003_login_ddt *******")


'''
Output is 
(.venv) olakoya@MacBookPro HybridFramework % pytest -s -v --browser chrome testCases/test_003_login_ddt.py

========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/PythonProject/HybridFramework/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}}
rootdir: /Users/olakoya/Desktop/PythonProject/HybridFramework/testCases
configfile: pytest.ini
plugins: html-4.1.1, metadata-3.1.1, xdist-3.6.1
collected 1 item                                                                                                                                                      

testCases/test_003_login_ddt.py::Test_Login_DDT::test_login_ddt Launching Chrome Browser.........
PASSED

------------------------ Generated html report: file:///Users/olakoya/Desktop/PythonProject/HybridFramework/reports/26-05-2025%2020-25-46.html ------------------------
========================================================================= 1 passed in 52.57s ==========================================================================
(.venv) olakoya@MacBookPro HybridFramework % 

'''