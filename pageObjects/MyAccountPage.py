from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyAccountPage:
    lnk_logout_xpath = "//aside//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_logout_xpath))
        ).click()
