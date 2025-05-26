import os
import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.utils import capture_screenshot
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_AccountReg:
    baseURL = "https://tutorialsninja.com/demo/index.php?route=common/home"
    logger = LogGen.loggen() # Creating a class variable for LogGen
    @pytest.mark.regression

    def test_account_reg(self, setup):
        self.logger.info("****test_001_AccountRegistration started****")
        self.driver = setup # Setting up for instant variable
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.logger.info("****Launching Application****")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("****Click on MyAccount ==> Register****")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Welsh")
        # self.regpage.setEmail(ReadConfig.getUseremail())

        # self.regpage.setEmail("alreadyregistered@example.com")  # Intentional fail
        self.email = randomString.random_string_generate() + '@gmail.com'
        self.regpage.setEmail(self.email)
        print("Used email:", self.email)

        self.regpage.setTelephone("07512345678")
        self.regpage.setPassword(ReadConfig.getPassword())
        self.regpage.setConfirmPassword(ReadConfig.getPassword())
        self.regpage.setPrivacyPolicy()

        time.sleep(3)
        self.regpage.clickContinue()
        print("Clicked Continue button")
        print("Current URL after registration:", self.driver.current_url)

        self.confmsg = self.regpage.getconfirmationmsg()
        print("Actual confirmation message:", repr(self.confmsg))

        #  This will take screenshot regardless of test result
        if self.confmsg == 'Your Account Has Been Created!':
            self.logger.info("****Account Registration is Passed****")
            capture_screenshot(self.driver, "text_account_reg")
            assert True
        else:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(os.path.join(os.getcwd()), 'screenshots', f'text_account_reg_{timestamp}.png')
            print("Saving screenshot to:", screenshot_path)
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("****Account Registration is Failed****")
            assert False, "Account Registration test failed"



'''
Output is
(.venv) olakoya@MacBookPro HybridFramework % pytest -s -v testCases/test_001_AccountRegistration.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/PythonProject/HybridFramework/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.6.1'}}
rootdir: /Users/olakoya/Desktop/PythonProject/HybridFramework
plugins: html-4.1.1, metadata-3.1.1, xdist-3.6.1
collected 1 item                                                                                                                                                      

testCases/test_001_AccountRegistration.py::Test_001_AccountReg::test_account_reg Used email: test17462146404751842@gmail.com
Actual confirmation message: Your Account Has Been Created!
PASSED

========================================================================= 1 passed in 10.18s ==========================================================================

'''

'''
Output after adding random and screenshots files
/Users/olakoya/Desktop/PythonProject/HybridFramework/.venv/bin/python /Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --target test_001_AccountRegistration.py::Test_001_AccountReg 
Testing started at 21:24 ...
Launching pytest with arguments test_001_AccountRegistration.py::Test_001_AccountReg --no-header --no-summary -q in /Users/olakoya/Desktop/PythonProject/HybridFramework/testCases

============================= test session starts ==============================
collecting ... collected 1 item

test_001_AccountRegistration.py::Test_001_AccountReg::test_account_reg 

============================== 1 passed in 9.20s ===============================
PASSED [100%]Used email: fgtsvxfv@gmail.com

Process finished with exit code 0

'''

'''
(.venv) olakoya@MacBookPro HybridFramework % pytest -s -v testCases/test_001_AccountRegistration.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/PythonProject/HybridFramework/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.6.1'}}
rootdir: /Users/olakoya/Desktop/PythonProject/HybridFramework
plugins: html-4.1.1, metadata-3.1.1, xdist-3.6.1
collected 1 item                                                                                                                                                      

testCases/test_001_AccountRegistration.py::Test_001_AccountReg::test_account_reg Used email: ithz0s1e@gmail.com
Actual confirmation message: Your Account Has Been Created!
Saving screenshot to: /Users/olakoya/Desktop/PythonProject/HybridFramework/screenshots/text_account_reg_{timestamp}.png
PASSED

========================================================================== 1 passed in 9.29s ==========================================================================

'''
'''
time of output: 21:15
.venv) olakoya@MacBookPro HybridFramework % pytest -s -v testCases/test_001_AccountRegistration.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/PythonProject/HybridFramework/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.6.1'}}
rootdir: /Users/olakoya/Desktop/PythonProject/HybridFramework
plugins: html-4.1.1, metadata-3.1.1, xdist-3.6.1
collected 1 item                                                                                                                                                      

testCases/test_001_AccountRegistration.py::Test_001_AccountReg::test_account_reg Used email: ocqe981e@gmail.com
Clicked Continue button
Current URL after registration: https://tutorialsninja.com/demo/index.php?route=account/success
Actual confirmation message: 'Your Account Has Been Created!'
Saving screenshot to: /Users/olakoya/Desktop/PythonProject/HybridFramework/screenshots/text_account_reg_20250503_211547.png
PASSED

========================================================================== 1 passed in 9.56s ==========================================================================
(.venv) olakoya@MacBookPro HybridFramework % 

'''