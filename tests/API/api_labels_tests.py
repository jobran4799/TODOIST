# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from infra.API.API_wrapper import APIWrapper
from logic.API.API_labels import labels



class labels_test(unittest.TestCase):
    ID = None
    def setUp(self):
        self.my_api = APIWrapper()
        self.test_p = labels(self.my_api)


    def test_get_personal_label(self):
        body = {"name": "Food"}
        my_c_api_temp = self.test_p.create_new_personal_label(body)
        json_response_temp = my_c_api_temp.json()
        self.ID = json_response_temp["id"]
        my_c_api = self.test_p.get_personal_label(self.ID)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["name"], "Food", "not equals")
        self.assertEqual(json_response["is_favorite"], False, "not equals")


    def test_update_a_personal_label(self):
        body = {"name": "Food"}
        my_c_api_temp = self.test_p.create_new_personal_label(body)
        json_response_temp = my_c_api_temp.json()
        self.ID = json_response_temp["id"]
        body = {"name": "milk"}
        my_c_api = self.test_p.update_a_personal_label(self.ID, body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["name"], "milk", "not equals")

    def tearDown(self):
        my_c_api = self.test_p.delete_label(self.ID)


