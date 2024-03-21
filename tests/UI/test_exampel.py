import time
import unittest

from infra.UI.Brawser_Wrapper import BrowserWrapper
from logic.UI.Log_in_page import LoginPage
from logic.UI.Main_page import MainPage




class test_example(unittest.TestCase):
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(self.browser)

    # def test_invalid_password_login(self):
    #     test_invalid_login = LoginPage(self.driver)
    #     test_invalid_login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm678")
    #     test_invalid_login.wrong_massage()
    #     time.sleep(4)
    #     self.assertTrue(test_invalid_login.wrong_massage.text.strip() == "Wrong email or password.",
    #                     "Message does not match")
    #
    # def test_Task_set_due_data(self):
    #     login = LoginPage(self.driver)
    #     login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
    #     main_page = MainPage(self.driver)
    #     main_page.set_due_date_task()
    #     time.sleep(4)
    #     self.assertTrue(main_page, "data did not be modified")
    #
    #
    # def test_Project_creation(self):
    #     login = LoginPage(self.driver)
    #     login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
    #     main_page = MainPage(self.driver)
    #     main_page.create_project("test add Project", True)
    #     time.sleep(4)
    #     self.assertTrue(main_page, "No match between the tasks name")
    def test_Project_to_find(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.find_project()
        self.assertTrue(main_page, "No match between the tasks name")

    def tearDown(self):
        self.driver.quit()