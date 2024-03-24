import pytest
import time
from selenium.common.exceptions import NoSuchElementException

from infra.utils import Utiles
from logic.UI.Main_page import MainPage

@pytest.mark.usefixtures("setup")
class TestMainPage:
    ISDELETED = False
    ID = None

    def test_task_creation(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        main_page = MainPage(driver)
        main_page.create_task(task_name)
        main_page = MainPage(driver)
        main_page.create_task(task_name)

    @pytest.mark.test_task_compilation
    def test_task_compilation(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        task_id = json_response["id"]
        self.ISDELETED = True
        main_page = MainPage(driver)
        main_page.click_completed_task(task_name)

    def test_task_editing(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        task_id = json_response["id"]
        main_page = MainPage(driver)
        main_page.edit_task(task_name)

    def test_task_priority(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        task_id = json_response["id"]
        main_page = MainPage(driver)
        main_page.priority_task(task_name)

    def test_Task_deletion(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        self.ISDELETED = True
        time.sleep(5)
        main_page = MainPage(driver)
        main_page.delete_task(task_name)

    def test_Task_set_due_data(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        main_page = MainPage(driver)
        main_page.set_due_date_task(task_name)