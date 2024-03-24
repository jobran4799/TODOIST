# test_runner.py
import json
import unittest
from infra.UI.Brawser_Wrapper import BrowserWrapper
from tests.UI.Main_Page_Test import TestMainPage

try:
    with open('config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run

list_test_cases_runer = [TestMainPage]


def test_brawser_runer():
    for test_cases in list_test_cases_runer:
        # test_cases.browser = browser
        test_suite = unittest.TestLoader().loadTestsFromTestCase(test_cases)
        print(test_suite)
        unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    browser_wrapper = BrowserWrapper()
    get_browser = data["browser"]
    test_brawser_runer()
