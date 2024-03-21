import unittest
import time

from infra.API.API_wrapper import APIWrapper
from infra.UI.Brawser_Wrapper import BrowserWrapper
from logic.API.API_tasks import Tasks
from logic.UI.Log_in_page import LoginPage
from logic.UI.Main_page import MainPage


class Main_page_test(unittest.TestCase):
    ID = None
    ISDELETED = False
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(self.browser)
        self.my_api = APIWrapper()
        self.test_p = Tasks(self.my_api)
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")

    # def test_Task_creation(self):
    #     main_page = MainPage(self.driver)
    #     main_page.creat_task("add test on todoist task")
    #     my_c_api = self.test_p.get_active_tasks()
    #     json_response = my_c_api.json()
    #     self.ID = json_response[0]["id"]
    #     time.sleep(2)
    #     self.assertTrue(main_page, "No match between the tasks name")
    #
    # # def test_Task_deletion(self):
    # #     body = {"content": "test on todoist task", "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
    # #     my_c_api = self.test_p.create_tasks(body)
    # #     json_response = my_c_api.json()
    # #     self.ID = json_response["id"]
    # #     self.ISDELETED = True
    # #     time.sleep(5)
    # #     main_page = MainPage(self.driver)
    # #     main_page.delete_task()
    # #     time.sleep(2)
    # #     self.assertTrue(main_page, "task is still exist")

    def test_Task_compilation(self):
        body = {"content": "test Completed task", "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = self.test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        time.sleep(2)
        main_page = MainPage(self.driver)
        main_page.set_complation_task("test Completed task")
        time.sleep(2)
        self.ISDELETED = True
        self.assertTrue(main_page, "task is not completed")
        # Wait for the task to be added

    def test_Task_editing(self):
        body = {"content": "test task editing", "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = self.test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        main_page = MainPage(self.driver)
        main_page.edit_task("test edit is working")
        time.sleep(2)
        self.assertTrue(main_page, "task is not add descrption")

    # def test_Task_priority(self):
    #     body = {"content": "task to change priority", "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
    #     my_c_api = self.test_p.create_tasks(body)
    #     json_response = my_c_api.json()
    #     self.ID = json_response["id"]
    #     main_page = MainPage(self.driver)
    #     main_page.priority_task()
    #     self.assertTrue(main_page, "priority does not modified")
    #
    # def test_Task_set_due_data(self):
    #     body = {"content": "task set due data", "due_string": "today at 12:00", "due_lang": "en", "priority": 3}
    #     my_c_api = self.test_p.create_tasks(body)
    #     json_response = my_c_api.json()
    #     self.ID = json_response["id"]
    #     main_page = MainPage(self.driver)
    #     main_page.set_due_date_task()
    #     self.assertTrue(main_page, "data did not be modified")


    def tearDown(self):
        if not self.ISDELETED:
            my_c_api = self.test_p.delete_tasks(self.ID)
        self.driver.quit()
