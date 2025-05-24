from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
        time.sleep(1)  # Optional: helps if there's a dropdown animation

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.lnk_login_linktext))
        ).click()