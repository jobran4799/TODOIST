# test_runner.py
import json
import unittest
from infra.UI.Brawser_Wrapper import BrowserWrapper
from api_parallel_tests import api_parallel_tests

# try:
#     with open('../../config.json') as f:
#         data = json.load(f)
# except FileNotFoundError:
#     print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
#     raise  # Raise the error to halt execution if the file is essential for the script to run

list_test_cases_runer = [api_parallel_tests]
def test_brawser_runer(browser):
    for test_cases in list_test_cases_runer:
        test_cases.browser = browser
        test_suite = unittest.TestLoader().loadTestsFromTestCase(test_cases)
        print(test_suite, browser)
        unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    browser_wrapper = BrowserWrapper()
    # cur_dir = os.path.abspath(__file__)
    # config_location = os.path.join(cur_dir, 'config.json')
    with open('config.json') as f:
        data = json.load(f)
    parallel = data["parallel"]
    serial = data["serial"]
    get_browser = data["browser"]
    browsers = data["browser_types"]
    if serial:
        for browser in browsers:
            test_brawser_runer(browser)
    else:
        test_brawser_runer(get_browser)
