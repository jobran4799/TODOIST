# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from infra.API.API_wrapper import APIWrapper
from infra.UI.Brawser_Wrapper import BrowserWrapper
from logic.API.API_projects import Project
from logic.UI.Log_in_page import LoginPage
from logic.UI.Main_page import MainPage


class api_parallel_tests(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(self.browser)

    def test_2(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.find_project()
        self.assertTrue(main_page, "No match between the tasks name")

    def test_1(self):
        test_p = Project(self.my_api)
        body ={"name": "final project"}
        my_c_api = test_p.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["name"], "final project", "not equals")



    def tearDown(self):
        self.driver.quit()

    # def test_get_all_collaborators(self):
    #     test_p = Project(self.my_api)
    #     my_c_api = test_p.Get_project_all_collaborators("2330262062")
    #     json_response = my_c_api.json()
    #     self.assertTrue(my_c_api.ok, "not ok")
    #     self.assertEqual(json_response[0]["name"], "Beyonddev", "not equals")
    #     self.assertEqual(json_response[0]["email"], "beyonddevtestproject@gmail.com", "not equals")
    #
    # def test_add_section_to_project(self):
    #     test_p = Section(self.my_api)
    #     body = {"project_id": "2330262062",
    #             "name": "section to delete"}
    #     my_c_api = test_p.add_section_to_project_by_id(body)
    #     json_response = my_c_api.json()
    #     self.assertTrue(my_c_api.ok, "not ok")
    #     self.assertEqual(json_response["project_id"], "2329678566", "not equals")
    #     self.assertEqual(json_response["name"], "section to delete", "not equals")
    #
    # def test_get_data_section_list(self):
    #     test_p = Section(self.my_api)
    #     my_c_api = test_p.get_all_sections("2330262062")
    #     json_response = my_c_api.json()
    #     self.assertTrue(my_c_api.ok, "not ok")
    #     self.assertEqual(json_response[0]["order"], 1, "not equals")
    #     self.assertEqual(json_response[0]["name"], "section to delete", "not equals")
    #
    #
    #
    # def test_name_section_update(self):
    #     test_p = Section(self.my_api)
    #     body = {"name": "Supermarket"}
    #     my_c_api = test_p.update_name_section("150550786", body)
    #     json_response = my_c_api.json()
    #     self.assertTrue(my_c_api.ok, "not ok")
    #     self.assertEqual(json_response["name"], "Supermarket", "not equals")
    #
    #
    # def test_get_active_tasks(self):
    #     test_p = Tasks(self.my_api)
    #     my_c_api = test_p.get_active_tasks()
    #     self.assertTrue(my_c_api.ok, "not deleted")
    #
    #
    # def test_update_tasks(self):
    #     test_p = Tasks(self.my_api)
    #     body = {"content": "Buy Coffee"}
    #     my_c_api = test_p.update_tasks("Buy Milk", body)
    #     json_response = my_c_api.json()
    #     self.assertTrue(my_c_api.ok, "not deleted")
    #     self.assertEqual(json_response["content"], "Buy Coffee", "not equals")
    #
    #
    # def test_update_a_personal_label(self):
    #     test_p = labels(self.my_api)
    #     body = {"name": "milk"}
    #     my_c_api = test_p.update_a_personal_label("2171988630", body)
    #     json_response = my_c_api.json()
    #     self.assertTrue(my_c_api.ok, "not deleted")
    #     self.assertEqual(json_response["name"], "milk", "not equals")




