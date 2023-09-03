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


class Herokuapp_TestCase(unittest.TestCase):

    # Setup for Unittest TestCase
    @classmethod
    def setUp(self):
        ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://the-internet.herokuapp.com/")
        self.wait = WebDriverWait(self.driver, 10)

###################################################

    def test_A_B_Variation(self): # Testing Site Variation
        self.driver.find_element(By.LINK_TEXT, "A/B Testing").click()
        variation_text = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/h3").text
        if variation_text == "A/B Test Variation 1":
            assert variation_text == "A/B Test Variation 1" , "Variation 1 was tested!"
        elif variation_text == "A/B Test Control":
            assert variation_text == "A/B Test Control" , "Variation 2 was tested!"
        else:
            self.fail("Neither of the variations were found")


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
        self.driver.find_element(By.LINK_TEXT, "Multiple Windows").click()
        self.driver.find_element(By.LINK_TEXT, "Click Here").click()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        page_check = self.driver.find_element(By.XPATH, "/html/body/div/h3").text
        assert page_check == "New Window"


    def test_Notification_Messages(self):
        self.driver.find_element(By.LINK_TEXT, "Notification Messages").click()
        notification_check = self.driver.find_element(By.ID, "flash").text
        while "Action successful" not in notification_check:
            self.driver.find_element(By.LINK_TEXT, "Click here").click()
            notification_check = self.driver.find_element(By.ID, "flash").text
        assert notification_check.__contains__("successful")


    def test_Disappearing_Elements(self):
        self.driver.find_element(By.LINK_TEXT, "Disappearing Elements").click()
        element_check = "Element not found yet."
        while element_check != "Gallery":
            try:
                self.driver.implicitly_wait(0.1)
                find_element = self.driver.find_element(By.LINK_TEXT, "Gallery")
                if element_check != "Gallery":
                    element_check = find_element.text
            except NoSuchElementException:
                self.driver.refresh()
        assert element_check == "Gallery"

########################################################

    # Teardown function for Unittest TestCase
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()