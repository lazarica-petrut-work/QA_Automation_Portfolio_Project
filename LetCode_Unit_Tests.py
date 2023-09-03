import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




class SauceDemo_TestCase(unittest.TestCase):

    # Setup for Unittest TestCase
    @classmethod
    def setUp(self):
        ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://letcode.in/test")
        self.wait = WebDriverWait(self.driver, 10)

###################################################

    def test_123(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-test-site/section[2]/div/div/div/div[2]/app-menu/div/footer/a").click()
        time.sleep(3)
        pass

























########################################################

    # Teardown function for Unittest TestCase
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()