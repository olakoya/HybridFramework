from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountRegistrationPage():
    # Locators
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_telephone_name = "telephone"
    txt_password_name = "password"
    txt_confpassword_name = "confirm"
    chk_policy_name = "agree"
    btn_cont_xpath="//input[@value='Continue']"
    text_msg_conf_xpath = "//h1[normalise-space()='Your Account Has Benn Created!']"

    # Constructor and Action Method
    def __init__(self,driver): # constructor has a 'driver' variable
        self.driver = driver

    def setFirstName(self, fname): # fname etc are parameters
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname) # send_keys represent test data

    def setLastName(self, lname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setTelephone(self, tel):
        self.driver.find_element(By.NAME, self.txt_telephone_name).send_keys(tel)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

    def setConfirmPassword(self, cnfpwd):
        self.driver.find_element(By.NAME, self.txt_confpassword_name).send_keys(cnfpwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.chk_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()

    def getconfirmationmsg(self): # installing variables in the confirmation message test case
        try:
            message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1"))
            )
            return message.text
        except Exception as e:
            print("Could not get confirmation message:", e)
            return ""
        # try:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Your Account Has Been Created!")
        #     )
        #     return element.text
        # except Exception as e:
        #     print(f"Could not get confirmation message: {e}")
        #     return ""




