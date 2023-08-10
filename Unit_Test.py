import time
import unittest

from selenium import webdriver
#Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By


class EmagTestCase(unittest.TestCase):

    # Setup for Unittest TestCase
    @classmethod
    def setUp(self):
        ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        #FirefoxService(GeckoDriverManager().install())
        #self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://the-internet.herokuapp.com/")


########################################################

    def test_navbar_dropdown(self):
        self.driver.find_element(By.ID, "nav-hamburger-menu").click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/ul[1]/li[7]/a/div").click()
        self.driver.find_element(By.LINK_TEXT, "/s?bbn=16225009011&rh=i%3Aspecialty-aps%2Cn%3A%2116225009011%2Cn%3A281407&ref_=nav_em__nav_desktop_sa_intl_accessories_and_supplies_0_2_5_2").click()



    def test_add_to_cart(self):
        self.driver.find_element(By.XPATH, '//*[@id="auxiliary"]/div/div/ul[2]/li[1]/a').click()
        assert self.driver.current_url == "https://www.emag.ro/nav/deals?ref=hdr_ofertele-emag"

    def test_bacanie(self):
        self.driver.find_element(By.XPATH, '//*[@id="auxiliary"]/div/div/ul[1]/li/div').click()
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/ul/li[7]/a/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="emg-body-overlay"]/div[2]/div[2]/div/div[3]/aside/ul[1]/li[2]/a').click()
        assert self.driver.current_url == "https://www.emag.ro/bauturi-alcoolice/sd?tree_ref=3860&ref=dep_cat_tree_199"

    # Teardown function for Unittest TestCase
    @classmethod
    def tearDown(self): # Sau tearDownClass
        self.driver.quit()
