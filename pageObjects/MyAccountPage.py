from selenium.webdriver.common.by import By

class MyAccountPage():
    # Locator
    lnk_logout_xpath = "(//a[text()='Logout'])[2]"
    # Constructor
def __init__(self,driver):
    self.driver = driver
    # Action Method
def clickLogout(self):
    self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()