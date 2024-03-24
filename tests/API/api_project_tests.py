# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from infra.API.API_wrapper import APIWrapper
from logic.API.API_projects import Project



class Projects_tests(unittest.TestCase):
    ID = None
    def setUp(self):
        self.my_api = APIWrapper()
        self.test_p = Project(self.my_api)


    def test_creat_project(self):
        body ={"name": "Shopping List"}
        my_c_api = self.test_p.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["name"], "Shopping List", "not equals")

    def test_update_project(self):
        body = {"name": "Shopping List"}
        my_c_api = self.test_p.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        body = {"name": "Things To Buy"}
        my_c_api = self.test_p.update_project_by_id(self.ID, body)
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["name"], "Shopping List", "not equals")

    def test_get_project(self):
        body = {"name": "Project task"}
        my_c_api = self.test_p.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        my_c_api = self.test_p.get_project_by_id(self.ID)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[0]["color"], "charcoal", "not equals")
        self.assertEqual(json_response[-1]["name"], "Project task", "not equals")

    def test_get_all_collaborators(self):
        body = {"name": "Project collaborators"}
        my_c_api = self.test_p.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        my_c_api = self.test_p.Get_project_all_collaborators(self.ID)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[0]["name"], "Beyonddev", "not equals")
        self.assertEqual(json_response[0]["email"], "beyonddevtestproject@gmail.com", "not equals")

    def tearDown(self):
        my_c_api = self.test_p.delete_project_by_id(self.ID)



