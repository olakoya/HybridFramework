import pytest
from numpy.f2py.rules import options
from selenium import webdriver

@pytest.fixture()
def setup(): # Passing fixture function
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()