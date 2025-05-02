import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString

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
    #   email = f"test{str(time.time()).replace('.', '')}@gmail.com"

        self.email = randomString.random_string_generate() + '@gmail.com'
        self.regpage.setEmail(self.email)
        print("Used email:", self.email)

    #   self.regpage.setEmail("test123123123@gmail.com")
        self.regpage.setTelephone("07512345678")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()

        time.sleep(3)
        self.regpage.clickContinue()

        self.confmsg = self.regpage.getconfirmationmsg()

    #    print("Actual confirmation message:", self.confmsg)

        if self.confmsg == 'Your Account Has Been Created!':
            assert True
        else:
            # self.driver.save_screenshot(os.path.dirname(os.getcwd())+'\\screenshots\\'+'text_account_reg.png')
            # screenshot_path = os.path.join(os.path.dirname(os.getcwd()), 'screenshots', 'test_account_reg.png')
            # self.driver.save_screenshot(screenshot_path)

            screenshot_path = os.path.join(os.path.dirname(os.getcwd()), 'screenshots', 'text_account_reg.png')
            print("Saving screenshot to:", screenshot_path)
            self.driver.save_screenshot(screenshot_path)

            if self.confmsg == 'Your Account Has Been Created!':
                assert True
            else:
                assert False

            assert False


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