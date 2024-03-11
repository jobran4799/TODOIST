# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from infra.API.API_wrapper import APIWrapper
from logic.API.API_tasks import Tasks


class task_tests(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.test_p = Tasks(self.my_api)

    def test_get_active_tasks(self):
        my_c_api = self.test_p.get_active_tasks()
        json_response = my_c_api.json()
        due_date = json_response[9]["due"]
        date = due_date["date"]
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response[9]["content"], "task set due data", "not equals")
        self.assertEqual(date, "2024-04-08", "not equals")

    def test_create_new_tasks(self):
        body = {"content": "Buy Milk", "due_string": "tomorrow at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = self.test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["content"], "Buy Milk", "not equals")
        self.assertEqual(json_response["priority"], 4, "not equals")

    def test_update_tasks(self):
        body = {"content": "Buy Coffee"}
        my_c_api = self.test_p.update_tasks("7775320373", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["content"], "Buy Coffee", "not equals")

    def test_delete_tasks(self):
        my_c_api = self.test_p.delete_tasks("7775337313")
        self.assertTrue(my_c_api.ok, "not deleted")





