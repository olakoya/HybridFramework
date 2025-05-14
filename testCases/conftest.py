import os.path
from pytest_metadata.plugin import metadata_key
import pytest
from numpy.f2py.rules import options
from selenium import webdriver
from datetime import datetime

# @pytest.fixture()
# def setup(): # Passing fixture function
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()

@pytest.fixture()
def setup(browser): # Passing fixture function
        if browser == 'edge':
            options = webdriver.EdgeOptions()
            options.add_experimental_option("detach", True)
            driver = webdriver.Edge(options=options)
            print("Launching Edge Browser.........")
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)
            print("Launching Firefox Browser.........")
        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options)
            print("Launching Chrome Browser.........")
        yield driver
        driver.quit()

def pytest_addoption(parser): # This will get the value from CLI/Hooks
    parser.addoption('--browser')

@pytest.fixture()
def browser(request): # This will return the Browser value to setup method
    return request.config.getoption('--browser')

# It is hook for adding Environment info to HTML report
def pytest_configure(config): # For adding information hook isn't required
    config.stash[metadata_key]['Project Name'] = 'Tutorial Ninja'
    config.stash[metadata_key]['Module Name'] = 'CustRegistration'
    config.stash[metadata_key]['Tester Name'] = 'Ola'

# It is hook for delete/modify Environment info to HTML report
@pytest.hookimpl(optionalhook=True)
# @pytest.mark.optionalhook # Deprecated
def pytest_metadata(metadata): # For modifying hook is required above
    metadata.pop("Python", None)  # pop means remove or delete
    metadata.pop("Plugins", None)

# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = (os.path.dirname(os.getcwd()) + "//HybridFramework//reports//"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html")
    # Your existing code