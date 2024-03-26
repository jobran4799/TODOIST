
import unittest
from infra.API.API_wrapper import APIWrapper
from logic.API.API_projects import Project
from logic.API.API_sections import Section


class api_parallel_tests(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()


    def test_get_all_collaborators(self):
        test_p = Project(self.my_api)
        my_c_api = test_p.Get_project_all_collaborators("2330262062")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[0]["name"], "Beyonddev", "not equals")
        self.assertEqual(json_response[0]["email"], "beyonddevtestproject@gmail.com", "not equals")

    def test_add_section_to_project(self):
        test_p = Section(self.my_api)
        body = {"project_id": "2330262062",
                "name": "section to delete"}
        my_c_api = test_p.add_section_to_project_by_id(body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["project_id"], "2329678566", "not equals")
        self.assertEqual(json_response["name"], "section to delete", "not equals")

    def test_get_data_section_list(self):
        test_p = Section(self.my_api)
        my_c_api = test_p.get_all_sections("2330262062")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[0]["order"], 1, "not equals")
        self.assertEqual(json_response[0]["name"], "section to delete", "not equals")



    def test_name_section_update(self):
        test_p = Section(self.my_api)
        body = {"name": "Supermarket"}
        my_c_api = test_p.update_name_section("150550786", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["name"], "Supermarket", "not equals")










