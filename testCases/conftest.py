import os
from datetime import datetime
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from pytest_metadata.plugin import metadata_key

# Add custom CLI options
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "edge", "firefox"], help="Browser to test")
    parser.addoption("--os", default="mac", choices=["windows", "mac", "linux"], help="Operating System to test")

# Parse CLI options into a tuple
@pytest.fixture()
def browser_platform(request):
    browser = request.config.getoption("--browser")
    platform = request.config.getoption("--os")
    return browser, platform

# Main fixture for driver setup
@pytest.fixture()
def setup(browser_platform):
    browser, platform = browser_platform
    baseenv = ReadConfig.getEnvironment()  # 'local' or 'remote'

    if baseenv == "remote":
        options_map = {
            "chrome": webdriver.ChromeOptions,
            "edge": webdriver.EdgeOptions,
            "firefox": webdriver.FirefoxOptions
        }

        if browser not in options_map:
            raise ValueError(f"Unsupported browser: {browser}")

        opt = options_map[browser]()
        if browser in ["chrome", "edge"]:
            opt.add_experimental_option("detach", True)

        platform_mapping = {"mac": "MAC", "windows": "WIN10", "linux": "LINUX"}
        platform_name = platform_mapping.get(platform.lower())
        if not platform_name:
            raise ValueError(f"Unsupported platform: {platform}")

        opt.set_capability("platformName", platform_name)

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=opt
        )
        print(f"Launching {browser.capitalize()} on Selenium Grid ({platform})...")

    else:  # Local execution
        if browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_experimental_option("detach", True)
            driver = webdriver.Edge(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)
        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)

        print(f"Launching {browser.capitalize()} browser locally...")

    yield driver
    driver.quit()

# Hooks for HTML report metadata and to add environment info to HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # report_dir = os.path.dirname(os.getcwd()) + "//HybridFramework//reports//"
    report_dir = os.path.join(os.path.dirname(__file__), 'reports')
    timestamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    config.option.htmlpath = os.path.join(report_dir, f"{timestamp}.html")

    if hasattr(config, "_metadata"):
        config._metadata['Project Name'] = 'Tutorial Ninja'
        config._metadata['Module Name'] = 'CustRegistration'
        config._metadata['Tester Name'] = 'Ola'

    # config.stash[metadata_key]['Project Name'] = 'Tutorial Ninja'
    # config.stash[metadata_key]['Module Name'] = 'CustRegistration'
    # config.stash[metadata_key]['Tester Name'] = 'Ola'


# Hook to clean up unnecessary metadata
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Python", None)
    metadata.pop("Plugins", None)




# First Conftest commanline
# @pytest.fixture()
# def setup(browser): # Passing fixture function
#
#         if browser == 'edge':
#             options = webdriver.EdgeOptions()
#             options.add_experimental_option("detach", True)
#             driver = webdriver.Edge(options=options)
#             driver.maximize_window()
#             print("Launching Edge Browser.........")
#
#         elif browser == 'firefox':
#             options = webdriver.FirefoxOptions()
#             driver = webdriver.Firefox(options=options)
#             driver.maximize_window()
#             print("Launching Firefox Browser.........")
#
#         else:
#             options = webdriver.ChromeOptions()
#             options.add_experimental_option("detach", True)
#             options.add_argument("--start-maximized")
#             driver = webdriver.Chrome(options=options)
#             print("Launching Chrome Browser.........")
#
#         yield driver
#         driver.quit()
#
# def pytest_addoption(parser): # This will get the value from CLI/Hooks
#     parser.addoption('--browser')
#
# @pytest.fixture()
# def browser(request): # This will return the Browser value to setup method
#     return request.config.getoption('--browser')
#
# # It is hook for adding Environment info to HTML report
# def pytest_configure(config): # For adding information hook isn't required
#     config.stash[metadata_key]['Project Name'] = 'Tutorial Ninja'
#     config.stash[metadata_key]['Module Name'] = 'CustRegistration'
#     config.stash[metadata_key]['Tester Name'] = 'Ola'
#
# # It is hook for delete/modify Environment info to HTML report
# @pytest.hookimpl(optionalhook=True)
# # @pytest.mark.optionalhook # Deprecated
# def pytest_metadata(metadata): # For modifying hook is required above
#     metadata.pop("Python", None)  # pop means remove or delete
#     metadata.pop("Plugins", None)
#
# # Specifying report folder location and save report with timestamp
# @pytest.hookimpl(tryfirst=True) # Using hook for one configuration which is used from the scratch to generate this report dynamically and it's automatically executed
# def pytest_configure(config):
#     config.option.htmlpath = (os.path.dirname(os.getcwd()) + "//HybridFramework//reports//"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html")
#     # Your existing code