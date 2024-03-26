import unittest
import time
from infra.API.API_wrapper import APIWrapper
from infra.UI.Brawser_Wrapper import BrowserWrapper
from infra.utils import Utiles
from logic.API.API_tasks import Tasks
from logic.UI.Log_in_page import LoginPage
from logic.UI.Main_page import MainPage


class Main_page_test(unittest.TestCase):
    ID = None
    ISDELETED = False
    BROWSER = None
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        if self.BROWSER == None:
            self.driver = self.browser_wrapper.get_driver("chrome")
        else:
            self.driver = self.browser_wrapper.get_driver(self.BROWSER)
        self.my_api = APIWrapper()
        self.test_p = Tasks(self.my_api)
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")

    def test_Task_creation(self):
        task_name = Utiles.generate_random_string(5)
        main_page = MainPage(self.driver)
        main_page.create_task(task_name)
        my_c_api = self.test_p.get_active_tasks()
        json_response = my_c_api.json()
        for get_id in json_response:
            if get_id["content"] == task_name:
                self.ID = get_id["id"]
        time.sleep(2)
        self.assertTrue(main_page, "No match between the tasks name")

    # def test_Task_deletion(self):
    #     task_name = Utiles.generate_random_string(5)
    #     body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
    #     my_c_api = self.test_p.create_tasks(body)
    #     json_response = my_c_api.json()
    #     self.ID = json_response["id"]
    #     main_page = MainPage(self.driver)
    #     main_page.delete_task(task_name)
    #     time.sleep(2)
    #     self.assertTrue(main_page, "task is still exist")
    #
    def test_Task_compilation(self):
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = self.test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        main_page = MainPage(self.driver)
        main_page.click_completed_task(task_name)
        time.sleep(2)
        self.assertTrue(main_page, "task is not completed")
        # Wait for the task to be added

    def test_Task_editing(self):
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = self.test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        main_page = MainPage(self.driver)
        main_page.edit_task(task_name)
        time.sleep(2)
        self.assertTrue(main_page, "task is not add descrption")

    # def test_Task_priority(self):
    #     task_name = Utiles.generate_random_string(5)
    #     body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
    #     my_c_api = self.test_p.create_tasks(body)
    #     json_response = my_c_api.json()
    #     self.ID = json_response["id"]
    #     main_page = MainPage(self.driver)
    #     main_page.priority_task(task_name, '3')
    #     self.assertTrue(main_page, "priority does not selected")
    #
    # def test_Task_set_due_data(self):
    #     task_name = Utiles.generate_random_string(5)
    #     body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
    #     my_c_api = self.test_p.create_tasks(body)
    #     json_response = my_c_api.json()
    #     self.ID = json_response["id"]
    #     main_page = MainPage(self.driver)
    #     main_page.set_due_date_task(task_name)
    #     self.assertTrue(main_page, "data did not be modified?")


    def tearDown(self):
        if not self.ISDELETED:
            my_c_api = self.test_p.delete_tasks(self.ID)
        if hasattr(self, '_outcome') and self._outcome.result:
            result = self._outcome.result
            if result.errors or result.failures:
                # If test fails, create a JIRA issue
                test_method_name = self._testMethodName
                error_message = ""
                for test, traceback_text in result.errors + result.failures:
                    error_message += f"Test: {test}\n"
                    error_message += f"Error: {traceback_text}\n"
                Utiles.create_jira_issue(f"{test_method_name} Test Failed", error_message)
        self.driver.quit()
