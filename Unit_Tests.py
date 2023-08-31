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
        self.wait = WebDriverWait(self.driver, 10)


###################################################
    # Testing Site Variation
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

    def test_Add_Elements(self):
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
        #Add
        add_element_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/button")))
        number_of_elements = 5
        for i in range(0, number_of_elements):
            add_element_button.click()
        #Check
        number_of_buttons_list = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        number_of_added_elements = 0
        for button in number_of_buttons_list:
            number_of_added_elements += 1
        assert number_of_added_elements == number_of_elements

    def test_Remove_Elements(self):
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
        #Add
        add_element_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/button")))
        number_of_elements = 5
        for i in range(0, number_of_elements):
            add_element_button.click()
        #Remove
        remove_button_list = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        number_of_present_elements = number_of_elements
        for button in remove_button_list:
            button.click()
            number_of_present_elements -= 1
        assert number_of_present_elements == 0

    def test_Basic_Authentication_Popup(self):
        #Login
        username = "admin"
        password = "admin"
        url = "http://"+ username +":"+ password + "@the-internet.herokuapp.com/basic_auth"
        self.driver.get(url)
        #Check
        string_variable = self.driver.find_element(By.CLASS_NAME, "example").text
        string_check = "Basic Auth"
        page_check = False
        if string_check in string_variable:
            page_check = True
        assert page_check == True

    def test_Checkbox(self):
        self.driver.find_element(By.LINK_TEXT, "Checkboxes").click()
        checkbox = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[1]")
        checkbox.click()
        is_checked = checkbox.is_selected()
        assert is_checked

    def test_Context_Menu(self):
        self.driver.find_element(By.LINK_TEXT, "Context Menu").click()
        context_box = self.driver.find_element(By.ID, "hot-spot")
        actions = ActionChains(self.driver)
        actions.context_click(context_box).perform()
        self.driver.switch_to.alert.accept()

    def test_Digest_Authentication(self):
        #Login
        self.driver.get("http://admin:admin@the-internet.herokuapp.com/digest_auth")
        # Check
        string_variable = self.driver.find_element(By.CLASS_NAME, "example").text
        string_check = "Digest Auth"
        page_check = False
        if string_check in string_variable:
            page_check = True
        assert page_check == True


    def test_Login_Page(self):
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        #Login
        username = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, "password")
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CLASS_NAME, "radius").click()
        #Check
        assert self.driver.current_url == "http://the-internet.herokuapp.com/secure"


    def test_Key_Presses(self):
        self.driver.find_element(By.LINK_TEXT, "Key Presses").click()
        self.driver.find_element(By.ID, "target").send_keys(Keys.SHIFT)
        self.driver.find_element(By.ID, "target").send_keys(Keys.TAB)
        result_check = self.driver.find_element(By.ID, "result").text
        assert result_check == "You entered: TAB", "A different key was pressed."



    def test_Multiple_Windows(self):
        pass

    def test_Notification_Messages(self):
        pass

    def test_Redirect_Link(self):
        pass #Poate

    def test_Slow_Resources(self):
        pass #Poate

    def test_Typos(self):
        pass

    def test_WYSIWYG_Editor(self):
        pass











########################################################

    # Teardown function for Unittest TestCase
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()