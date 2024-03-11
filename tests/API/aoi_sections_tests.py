# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from infra.API.API_wrapper import APIWrapper
from logic.API.API_sections import Section


class Section_test(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.test_p = Section(self.my_api)

    def test_add_section_to_project(self):
        body = {"project_id": "2329678566",
                "name": "section to delete"}
        my_c_api = self.test_p.add_section_to_project_by_id("2329678566", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["project_id"], "2329678566", "not equals")
        self.assertEqual(json_response["name"], "section to delete", "not equals")

    def test_get_data_section_list(self):
        my_c_api = self.test_p.get_all_sections("2329678566")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[0]["order"], 1, "not equals")
        self.assertEqual(json_response[0]["name"], "check section", "not equals")
        self.assertEqual(json_response[1]["id"], "149886499", "not equals")
        self.assertEqual(json_response[1]["name"], "postman", "not equals")

    def test_get_data_section(self):
        my_c_api = self.test_p.get_single_section("149886499")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["project_id"], "2329678566", "not equals")
        self.assertEqual(json_response["name"], "postman", "not equals")

    def test_name_section_update(self):
        body = {"name": "Supermarket"}
        my_c_api = self.test_p.update_name_section("149961566", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["name"], "Supermarket", "not equals")

    def test_delete_section(self):
        my_c_api = self.test_p.delete_section("149962796")
        self.assertTrue(my_c_api.ok, "not deleted")




