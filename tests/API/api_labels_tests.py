# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from infra.API.API_wrapper import APIWrapper
from logic.API.API_labels import labels



class labels_test(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.test_p = labels(self.my_api)


    def test_get_personal_label(self):
        my_c_api = self.test_p.get_personal_label("2171988630")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["name"], "Food", "not equals")
        self.assertEqual(json_response["is_favorite"], False, "not equals")

    def test_create_new_personal_label(self):
        body = {"name": "buffel"}
        my_c_api = self.test_p.create_new_personal_label(body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["name"], "buffel", "not equals")

    def test_update_a_personal_label(self):
        body = {"name": "milk"}
        my_c_api = self.test_p.update_a_personal_label("2171988630", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["name"], "milk", "not equals")

    def test_delete_label(self):
        my_c_api = self.test_p.delete_label("2171988718")
        self.assertTrue(my_c_api.ok, "not deleted")


