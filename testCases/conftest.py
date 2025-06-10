import os.path
from email.policy import default

from pytest_metadata.plugin import metadata_key
import pytest
from numpy.f2py.rules import options
from selenium import webdriver
from datetime import datetime
from utilities.readProperties import ReadConfig

@pytest.fixture()
def setup(browser_platform):
    baseenv = ReadConfig.getEnvironment()
    browser_platform = browser_platform
    if baseenv == "remote":
        options = {
            "chrome": webdriver.ChromeOptions,
            "edge": webdriver.EdgeOptions,
            "firefox": webdriver.FirefoxOptions
        }
        if browser not in options:
            raise ValueError(f"Unsupported browser:{browser}")
        platform_mapping = {"mac": "MAC", "windows": "Win10", "linux": "LINUX"}
        platform_name = platform_mapping.get(platform)
        if not platform_name:
            raise ValueError(f"Unsupported platform: {platform}")
        opt = options[browser]()
        opt.add_experimental_option("detach", True) if browser in ["chrome", "edge"] else None
        opt.platform_name = platform_name
        driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=opt)
    elif baseenv == "local":
        if browser == 'edge':
            options = webdriver.EdgeOptions()
            options.add_experimental_option("detach", True)
            driver = webdriver.Edge(options=options)
            print("Launching Edge browser.........")
        if browser == 'firefox':
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)
            print("Launching Edge browser.........")
        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options)
            print("Launching Chrome browser.........")
        yield driver
        driver.quit()

# Hook to add commandline options for browser and os
def pytest_addoption(parser): # This will get the value from CLI/Hooks
    parser.addoption("--browser", default="chrome", choices=["chrome", "edge", "firefox"], help = "Browser to test")
    parser.addoption("--os", default="mac", choices=["windows", "mac", "linux"], help = "Operating System to test")

# Get value from commandline
@pytest.fixture()
def browser_platform(request):
    browser = request.config.getoption("--browser")
    platform = request.config.getoption("--os")
    return browser,platform

#Hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Tutorial Ninja'
    config.stash[metadata_key]['Tester Name'] = 'Ola'

#Hook for Delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Python", None)
    metadata.pop("Plugins", None)

#Specifying Report Folder Locations and Save Report with Timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = (os.path.dirname(os.getcwd()) + "HybridFramework//reports//"+datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html")





# First Conftest commanline
@pytest.fixture()
def setup(browser): # Passing fixture function

        if browser == 'edge':
            options = webdriver.EdgeOptions()
            options.add_experimental_option("detach", True)
            driver = webdriver.Edge(options=options)
            driver.maximize_window()
            print("Launching Edge Browser.........")

        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()
            print("Launching Firefox Browser.........")

        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument("--start-maximized")
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
@pytest.hookimpl(tryfirst=True) # Using hook for one configuration which is used from the scratch to generate this report dynamically and it's automatically executed
def pytest_configure(config):
    config.option.htmlpath = (os.path.dirname(os.getcwd()) + "//HybridFramework//reports//"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html")
    # Your existing code