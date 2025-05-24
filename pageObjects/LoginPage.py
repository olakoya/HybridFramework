from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    # Locators
    txt_email_id = "input-email"
    txt_password_id = "input-password"
    btn_login_xpath = "//input[@value='Login']"
    my_account_xpath = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.txt_email_id))
        )
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).clear()
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.my_account_xpath).is_displayed()
        except:
            return False



# from selenium.webdriver.common.by import By
#
# class LoginPage(): # Creating an Object of Login Page Class
#     # Locators
#     txt_email_xpath = "//input[@id='input-email']"
#     txt_password_xpath = "//input[@id='input-password']"
#     btn_login_xpath = "//input[@value='Login']"
#     msg_myaccount_xpath = "//h2[text()='My Account']"
#
#     # Constructor
#     def __init__(self,driver):
#         self.driver=driver
#
#     # Action Methods
#     def setEmail(self, email):
#         self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)
#
#     def setPassword(self,pwd):
#         self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)
#
#     def clickLogin(self):
#         self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
#
#     def isMyAccountPageExists(self):
#         try:
#             return self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
#         except:
#             return False
