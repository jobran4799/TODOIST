from infra.API.API_wrapper import APIWrapper
from infra.UI.Brawser_Wrapper import BrowserWrapper
from infra.utils import Utiles
from logic.API.API_tasks import Tasks
from logic.UI.Log_in_page import LoginPage
from logic.UI.Main_page import MainPage

class TestMainPage:
    ID = None
    TODELETED = True
    # def setup_method(self):
    #     self.browser_wrapper = BrowserWrapper()
    #     self.driver = self.browser_wrapper.get_driver("chrome")
    #     self.my_api = APIWrapper()
    #     self.test_p = Tasks(self.my_api)
    #     login = LoginPage(self.driver)
    #     login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
    #
    # def teardown_method(self):
    #     if self.TODELETED:
    #         my_c_api = self.test_p.delete_tasks(self.ID)
    #     self.driver.quit()

    def test_task_creation(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        main_page = MainPage(driver)
        main_page.create_task(task_name)
        my_c_api = test_p.get_active_tasks()
        json_response = my_c_api.json()
        for get_id in json_response:
            if get_id["content"] == task_name:
                self.ID = get_id["id"]

    def test_task_priority(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        main_page = MainPage(driver)
        main_page.priority_task(task_name, '3')

    def test_task_deletion(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        main_page = MainPage(driver)
        main_page.delete_task(task_name)

    def test_task_set_due_date(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        main_page = MainPage(driver)
        main_page.set_due_date_task(task_name)

    def test_task_compilation(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        main_page = MainPage(driver)
        main_page.click_completed_task(task_name)

    def test_task_editing(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        main_page = MainPage(driver)
        main_page.edit_task(task_name)



