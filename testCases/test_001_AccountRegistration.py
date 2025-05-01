from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage

class Test_001_AccountReg:
    baseURL = "https://tutorialsninja.com/demo/index.php?route=common/home"
    def test_account_reg(self, setup):
        self.driver = setup # Setting up for instant variable
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Welsh")
        self.regpage.setEmail("test123123123@gmail.com")
        self.regpage.setTelephone("07512345678")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()

        print("Actual confirmation message:", self.confmsg)

        if self.confmsg == 'Your Account Has Been Created!':
            assert True
        else:
            assert False


