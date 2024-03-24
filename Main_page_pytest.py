import pytest
import time
from selenium.common.exceptions import NoSuchElementException

from infra.utils import Utiles
from logic.UI.Main_page import MainPage

@pytest.mark.usefixtures("setup")
class TestMainPage:

    def test_task_creation(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        main_page = MainPage(driver)
        main_page.create_task(task_name)
        # Add assertions here to verify task creation

    @pytest.mark.test_task_compilation
    def test_task_compilation(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        task_id = json_response["id"]
        # Add test logic here for task compilation

    def test_task_editing(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        task_id = json_response["id"]
        # Add test logic here for task editing

    def test_task_priority(self, setup):
        driver, test_p = setup
        task_name = Utiles.generate_random_string(5)
        body = {"content": task_name, "due_string": "today at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        task_id = json_response["id"]
        # Add test logic here for task priority