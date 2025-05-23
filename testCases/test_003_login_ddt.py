import time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
import os

class Test_DDT():
    baseURL = ReadConfig.getApplicationURL()  # Getting static methods in config class
    logger = LogGen.loggen() # Logger
    path = os.path.abspath(os.curdir)+"//testdata//Opencart_LoginData.xlsl"

    def test_login_ddt(self,setup):
        self.logger.info("****Starting test_003_login_Datadriven****")
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        lst_status = []
        self.driver = setup  # this method will return driver variable
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)
        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()
            self.email = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetpage = self.lp.isMyAccountPageExists()
            if self.exp == 'Valid':
                if self.targetpage == True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp == 'Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')
    # Final Validation
    if "Fail" not in lst_status:
        assert True
    else:
        assert False
        self.logger.info("******* End of test_003_login_Datadriven *******")