# test_runner.py
import json
import unittest

from infra.UI.Brawser_Wrapper import BrowserWrapper
from tests.UI.Log_In_Page_Test import Login_page_test
from tests.UI.Main_Page_Test import Main_page_test
from tests.UI.Projects_List_Page_Test import Project_List_Page_Test
from tests.UI.test_exampel import test_example

try:
    with open('config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run

list_test_cases_runer = [Login_page_test, Main_page_test, Project_List_Page_Test]
def test_brawser_runer(browser):
    for test_cases in list_test_cases_runer:
        test_cases.browser = browser
        test_suite = unittest.TestLoader().loadTestsFromTestCase(test_cases)
        print(test_suite, browser)
        unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    browser_wrapper = BrowserWrapper()
    get_browser = data["browser"]
    test_brawser_runer(get_browser)
