import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
#Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By


class SauceDemo_TestCase(unittest.TestCase):

    # Setup for Unittest TestCase
    @classmethod
    def setUp(self):
        ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(self.driver, 10)

###################################################

    def Login(self):
        #Username
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        #Passward
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        #Login Button
        self.driver.find_element(By.ID, "login-button").click()


    def Item_Selector(self, item_name):
        #Login
        self.Login()
        #Item Search
        item_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for item in item_list:
            if item.text == item_name:
                item.click()
                break
        #Add to cart
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/button").click()
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        cart_item = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        #Assert
        assert item_name == cart_item


    def test_Login(self):
        self.Login()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"


    def test_Sauce_Labs_Backpack(self):
        self.Item_Selector("Sauce Labs Backpack")


    def test_Sauce_Labs_Bike_Light(self):
        self.Item_Selector("Sauce Labs Bike Light")


    def test_Sauce_Labs_Bolt_T_Shirt(self):
        self.Item_Selector("Sauce Labs Bolt T-Shirt")


    def test_Sauce_Labs_Fleece_Jacket(self):
        self.Item_Selector("Sauce Labs Fleece Jacket")


    def test_Sauce_Labs_Onesie(self):
        self.Item_Selector("Sauce Labs Onesie")


    def test_Test_allTheThings_T_Shirt_Red(self):
        self.Item_Selector("Test.allTheThings() T-Shirt (Red)")


    def test_Checkout(self):
        self.Login()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("Hello")
        self.driver.find_element(By.ID, "last-name").send_keys("World")
        self.driver.find_element(By.ID, "postal-code").send_keys("123")
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"










########################################################

    # Teardown function for Unittest TestCase
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()