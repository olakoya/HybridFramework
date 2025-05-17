from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_login():
    baseURL = ReadConfig.getApplicationURL() # Getting static methods in config class
    logger = LogGen.loggen() # Class variable in Test Login
    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword() # Specific method get Password

    def test_login(self,setup):
        self.logger.info("****Starting test_002_login****")
        self.driver = setup # this method will return driver variable
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = HomePage(self.driver) # Creating Object of the HomePage hp
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver) # Landing on the Login Page lp which is an object of the loginpage
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            # self.driver.save_screenshot(os.path.abspath(os.getcwd())+"//screenshots//"+"test_account_log.png")
            print("Login failed. Current page:", self.driver.current_url)
            print("Page title:", self.driver.title)
            self.driver.save_screenshot("screenshots/test_account_log.png")
            # assert False
            assert self.targetpage, "Login failed: My Account page not found"
            self.logger.info("****End of test_002_login****")