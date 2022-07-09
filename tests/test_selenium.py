import time
import pytest
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=chrome_options)
    request.cls.driver = chrome_driver
    chrome_driver.get('http://localhost:7000/admin/')
    time.sleep(5)
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("chrome_driver_init")
class test_Browser1(LiveServerTestCase):
    def test_example(self):
        # self.driver.get('http://localhost:7000/admin/')
        # time.sleep(5)
        assert "Log in | Django site admin" in self.driver.title


#tests without fixture
# class testBrowser1 (LiveServerTestCase):
#     def test_example(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#
#         driver= webdriver.Chrome("./chromedriver",options=chrome_options)
#         # driver.get(("%s%s" %(self.live_server_url,"")))
#         driver.get('http://localhost:7000/admin/')
#         # time.sleep(5)
#         assert "Log in | Django site admin" in driver.title
