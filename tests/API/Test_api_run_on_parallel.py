# test_runner.py
import json
import unittest
from concurrent.futures import ThreadPoolExecutor
from infra.UI.Brawser_Wrapper import BrowserWrapper
from tests.API.api_parallel_tests import api_parallel_tests

try:
    with open('../../config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run


list_test_cases_runer = [api_parallel_tests]
def test_brawser_runer(browser):
    for test_cases in list_test_cases_runer:
        test_cases.browser = browser
        test_suite = unittest.TestLoader().loadTestsFromTestCase(test_cases)
        print(test_suite, browser)
        unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    browser_wrapper = BrowserWrapper()
    parallel = data["parallel"]
    browsers = data["browser_types"]
    if parallel:
        with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
            executor.map(test_brawser_runer, browsers)
