import pytest

from Main_page_pytest import TestMainPage
from infra.API.API_wrapper import APIWrapper
from infra.UI.Brawser_Wrapper import BrowserWrapper
from logic.API.API_tasks import Tasks
from logic.UI.Log_in_page import LoginPage


@pytest.fixture
def setup(request):
    browser_wrapper = BrowserWrapper()
    driver = browser_wrapper.get_driver("chrome")
    my_api = APIWrapper()
    test_p = Tasks(my_api)
    login = LoginPage(driver)
    login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")

    def teardown():
        if TestMainPage.TODELETED:
            my_c_api = test_p.delete_tasks(TestMainPage.ID)
        driver.quit()

    request.addfinalizer(teardown)
    return driver, test_p
