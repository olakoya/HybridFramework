import os
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

    def test_login_ddt(self, setup):
        self.logger.info("**** Starting Data Driven Test Case for Login ****")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet 1')
        lst_status = []
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2, self.rows + 1):
            self.logger.info(f"---------- Row {r} ----------")
            self.hp.clickMyAccount()

            # Wait for Login link
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            self.hp.clickLogin()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "input-email"))
            )

            email = XLUtils.readData(self.path, "Sheet 1", r, 1)
            password = XLUtils.readData(self.path, "Sheet 1", r, 2)
            expected_result = XLUtils.readData(self.path, "Sheet 1", r, 3)

            self.logger.info(f"Testing with Email: {email}, Password: {password}, Expected: {expected_result}")

            self.lp.setEmail(email)
            self.lp.setPassword(password)
            self.lp.clickLogin()

            # Wait for possible login redirect
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

        # Final assertion and logging
        if "Fail" not in lst_status:
            self.logger.info("All data-driven login tests passed.")
            assert True
        else:
            self.logger.error("Some data-driven login tests failed.")
            assert False

        self.logger.info("******* End of test_003_login_ddt *******")



# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pageObjects.HomePage import HomePage
# from pageObjects.LoginPage import LoginPage
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
# from pageObjects.MyAccountPage import MyAccountPage
# from utilities import XLUtils
# import os
#
# class Test_Login_DDT:
#     baseURL = ReadConfig.getApplicationURL()  # Getting static methods in config class
#     logger = LogGen.loggen() # Logger
#     path = os.path.abspath(os.curdir)+"//testData//Opencart_LoginData.xlsx"
#
#     def test_login_ddt(self,setup): # setup contains setup method
#         self.logger.info("****Starting of Data Driven Test Case****")
#         self.rows = XLUtils.getRowCount(self.path,'Sheet 1')
#         lst_status = []
#         self.driver = setup  # this method will return driver variable
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         self.hp = HomePage(self.driver)
#         self.lp = LoginPage(self.driver)
#         self.ma = MyAccountPage(self.driver)
#
#         for r in range(2,self.rows+1):
#             # Performing Click Action
#             self.hp.clickMyAccount()
#             WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
#             )
#
#             self.hp.clickLogin()
#             self.email = XLUtils.readData(self.path,"Sheet 1",r,1)
#             self.password = XLUtils.readData(self.path,"Sheet 1",r,2)
#             self.exp = XLUtils.readData(self.path,"Sheet 1",r,3)
#             self.lp.setEmail(self.email) # Passing data
#             self.lp.setPassword(self.password)
#             self.lp.clickLogin()
#             self.targetpage = self.lp.isMyAccountPageExists()
#
#             # Important Condition
#             if self.exp == 'Valid':
#                 if self.targetpage == True:
#                     lst_status.append("Pass")
#                     self.ma.clickLogout()
#                 else:
#                     lst_status.append("Fail")
#             elif self.exp == 'Invalid':
#                 if self.targetpage == True:
#                     lst_status.append('Fail')
#                     self.ma.clickLogout()
#                 else:
#                     lst_status.append('Pass')
#         # Final Validation
#         if "Fail" not in lst_status:
#             assert True
#         else:
#             assert False
#         self.logger.info("******* End of test_003_login_Datadriven *******")