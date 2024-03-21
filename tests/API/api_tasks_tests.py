# This is a sample Python script.
import unittest

from infra.API.API_wrapper import APIWrapper
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from logic.API.API_tasks import Tasks


class task_tests(unittest.TestCase):
    ID = None
    def setUp(self):
        self.my_api = APIWrapper()
        self.test_p = Tasks(self.my_api)

    def test_get_active_tasks(self):
        body = {"content": "Buy Milk", "due_string": "tomorrow at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = self.test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        my_c_api = self.test_p.get_active_tasks()
        self.assertTrue(my_c_api.ok, "not deleted")

    def test_update_tasks(self):
        body = {"content": "Buy Milk", "due_string": "tomorrow at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = self.test_p.create_tasks(body)
        json_response = my_c_api.json()
        body = {"content": "Buy Coffee"}
        my_c_api = self.test_p.update_tasks(json_response["id"], body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["content"], "Buy Coffee", "not equals")

    def test_create_new_tasks(self):
        body = {"content": "Buy Milk", "due_string": "tomorrow at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = self.test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["content"], "Buy Milk", "not equals")
        self.assertEqual(json_response["priority"], 4, "not equals")

    def test_create_new_tasks2(self):
        body = {"content": "Buy cheese", "due_string": "tomorrow at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = self.test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["content"], "Buy cheese", "not equals")
        self.assertEqual(json_response["priority"], 4, "not equals")

    def tearDown(self):
        my_c_api = self.test_p.delete_tasks(self.ID)
