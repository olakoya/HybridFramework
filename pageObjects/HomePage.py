from selenium.webdriver.common.by import By

# Creating Class and inside it contains locators
class HomePage:
    # Locators
    lnk_myaccount_xpath = "//span[text()='My Account']"
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"

# Creating a Constructor
    def __init__(self,driver): # constructor has a 'driver' variable
        self.driver = driver

# Creating a Click Action Methods
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_myaccount_xpath).click() # locator declared earlier in class

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()