import unittest

from infra.API.API_wrapper import APIWrapper
from infra.UI.Brawser_Wrapper import BrowserWrapper
from infra.utils import Utiles
from logic.API.API_projects import Project
from logic.UI.Log_in_page import LoginPage
from logic.UI.Main_page import MainPage
from logic.UI.Project_List_Page import ProjectListPage


class Project_List_Page_Test(unittest.TestCase):
    ID = None
    ISDELETED = False
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver('chrome')
        self.my_api = APIWrapper()
        self.test_p = Project(self.my_api)
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")

    def test_Project_creation(self):
        task_name = Utiles.generate_random_string(5)
        list_project = ProjectListPage(self.driver)
        list_project.create_project(task_name, True)
        my_c_api = self.test_p.get_all_project()
        json_response = my_c_api.json()
        self.ID = json_response[0]["id"]
        self.assertTrue(list_project, "No match between the tasks name")


    def test_Project_deletion(self):
        task_name = Utiles.generate_random_string(5)
        body = {"name": task_name}
        my_c_api = self.test_p.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.ID = json_response["id"]
        self.ISDELETED = False
        list_project = ProjectListPage(self.driver)
        list_project.delete_task(task_name)
        self.assertTrue(list_project, "No match between the tasks name")

    def tearDown(self):
        if not self.ISDELETED:
            my_c_api = self.test_p.delete_project_by_id(self.ID)
        self.driver.quit()
