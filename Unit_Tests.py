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


class TestCase(unittest.TestCase):

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


    #def test_firstbutton(self):
    #    time.sleep(1)
    #    self.driver.find_element(By.LINK_TEXT, "A/B Testing").click()
    #    time.sleep(1)

###################################################
    def test_A_B_Variation(self):
        self.driver.find_element(By.LINK_TEXT, "A/B Testing").click()
        #time.sleep(1)
        variation_text = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/h3").text
        #print(variation_text)
        if variation_text == "A/B Test Variation 1":
            assert variation_text == "A/B Test Variation 1" , "Variation 1 was tested!"
        elif variation_text == "A/B Test Control":
            assert variation_text == "A/B Test Control" , "Variation 2 was tested!"
        else:
            self.fail("Neither of the variations were found")
        #print(variation_text)






########################################################

    # Teardown function for Unittest TestCase
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()