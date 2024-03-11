# test_runner.py
import json
import unittest

from infra.UI.Brawser_Wrapper import BrowserWrapper
from tests.UI.test_exampel import test_example

try:
    with open('../../Config_Manegre/config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run

list_test_cases_runer = [test_example]
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
