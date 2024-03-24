# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from infra.API.API_wrapper import APIWrapper
from logic.API.API_sections import Section
from logic.API.API_projects import Project


class Section_test(unittest.TestCase):
    ID = None
    def setUp(self):
        self.my_api = APIWrapper()
        self.test_p = Section(self.my_api)
        self.test_project = Project(self.my_api)

    def test_add_section_to_project(self):
        body = {"name": "api project add sections"}
        my_c_api = self.test_project.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        body = {"project_id": self.ID,
                "name": "section to add"}
        my_c_api = self.test_p.add_section_to_project_by_id(body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["project_id"], self.ID, "not equals")
        self.assertEqual(json_response["name"], "section to add", "not equals")

    def test_get_data_section_list(self):
        body = {"name": "api project add sections"}
        my_c_api = self.test_project.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        body = {"project_id": self.ID,
                "name": "section to add"}
        my_c_api = self.test_p.add_section_to_project_by_id(body)
        body = {"project_id": self.ID,
                "name": "section to add2"}
        my_c_api = self.test_p.add_section_to_project_by_id(body)
        my_c_api = self.test_p.get_all_sections(self.ID)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[0]["name"], "section to add", "not equals")
        self.assertEqual(json_response[1]["name"], "section to add2", "not equals")

    def test_name_section_update(self):
        body = {"name": "api project add sections"}
        my_c_api = self.test_project.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        body = {"project_id": self.ID,
                "name": "section to add"}
        my_c_api_section = self.test_p.add_section_to_project_by_id(body)
        json_response_section = my_c_api_section.json()
        id = json_response_section["id"]
        body = {"name": "Supermarket"}
        my_c_api = self.test_p.update_name_section(id, body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["name"], "Supermarket", "not equals")

    def tearDown(self):
        my_c_api = self.test_project.delete_project_by_id(self.ID)




