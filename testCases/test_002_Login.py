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
        self.lp.setEmail(self.user) # Calling and passing data from the email and password with the help of statics method in utilities
        self.lp.setPassword(self.password)
        self.lp.clickLogin() # Calling some actions
        self.targetpage=self.lp.isMyAccountPageExists() # A TC must receive a valuation
        if self.targetpage==True:  # Returning true boolean value & Every TC will pass
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.getcwd())+"//screenshots//"+"test_account_log.png")
            assert False # Every TC will pass until put assertion
            self.logger.info("****End of test_002_login****")