import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from infra.UI.Base_Page import BasePage


class ProjectListPage(BasePage):
    FIND_MY_PROJECTS = (By.XPATH, "//button[@aria-label='My projects menu']")
    # FIND_CLICKER_TO_ADD_PROJECT = (By.XPATH, "//div[@class='a83bd4e0 e214ff2e fb8d74bb' and text()='Add project']")
    # INPUT_TEXT_ADD_PROJECT = (By.XPATH, "//input[@id='edit_project_modal_field_name']")
    # ADD_PROJECT_TO_FAVORITE = (By.XPATH,
    #                            "//div[contains(@class, '_618235b7') and contains(@class, 'fb8d74bb') and contains(@class, '_18f74af9') and contains(@class, '_68aab614')]/input[@name='is_favorite']")

    PROJECT_LIST_BUTTON = (By.XPATH,
                           "//div[contains(@class, 'qMjaCbb') and contains(@class, 'a83bd4e0') and contains(@class, '_7be5c531') and contains(@class, '_6a3e5ade') and contains(@class, '_2f303ac3') and contains(@class, 'fb8d74bb') and contains(@class, '_211eebc7') and text()='My Projects']")
    PROJECT_NAME = (By.XPATH,
                    "//ul[@id='projects_list']//span[@class='X_3UwghUggmfmKrS8M8uwnLl4hgJenHE a83bd4e0 _2f303ac3 fb8d74bb _211eebc7' and text()='final project']/ancestor::div[@class='pMTLzg8']")

    FIND_TASK_TO_DELETE =(By.XPATH,"(//ul[@aria-label='Projects']//li[@role='treeitem'])[1]")
    FIND_MORE_ACTIONS_BUTTON = (By.XPATH, "//div[./a[./div[./span[contains(text(),'aaa')]]]]//button[@aria-label='More project actions']")
    FIND_DELETE_REQUSET = (By.XPATH, "//div[contains(@class, 'a83bd4e0') and contains(@class, 'a8d37c6e') and contains(@class, '_2f303ac3') and contains(@class, 'fb8d74bb') and contains(@class, '_211eebc7') and text()='Delete']")
    FIND_DELETE_CONFRMATION = (By.XPATH,"//button[@class='_8313bd46 _7a4dbd5f _5e45d59f fb8d74bb _56a651f6']")


    def clicker_button(self, click):
        click.click()

    def fill_input(self, task_input, task_TaskName):
        time.sleep(2)
        task_input.send_keys(task_TaskName)
        time.sleep(2)

    def click_enter(self, write_input):
        write_input.send_keys(Keys.ENTER)

    def find_projects_list(self):
        self.project_list = self._driver.find_element(*self.FIND_MY_PROJECTS)

    def find_add_project_clicker(self):
        self.clicker_add_project = self._driver.find_element(By.XPATH, "//div[contains(@role,'menu')]//button[contains(@aria-label,'Add project')]")

    def find_input_project_name(self):
        self.input_project_name = self._driver.find_element(By.XPATH, "//input[contains(@id,'edit_project_modal_field_name')]")

    def find_clicker_to_favorite(self):
        self.add_project_to_favorite = self._driver.find_element(By.XPATH, "//input[contains(@name,'is_favorite')]")

    def action_prform_clicker(self, add_to_favorite):
        actions = ActionChains(self._driver)
        actions.move_to_element(add_to_favorite).click().perform()

    def action_prform_hover_over(self, hover_to_project):
        actions = ActionChains(self._driver)
        actions.move_to_element(hover_to_project).perform()

    def create_project(self, text_task_name, add_to_favorite):
        self.find_projects_list()
        self.clicker_button(self.project_list)
        time.sleep(2)
        self.find_add_project_clicker()
        self.clicker_button(self.clicker_add_project)
        time.sleep(2)
        self.find_input_project_name()
        self.fill_input(self.input_project_name, text_task_name)
        time.sleep(2)
        if add_to_favorite:
            self.find_clicker_to_favorite()
            self.action_prform_clicker(self.add_project_to_favorite)
        time.sleep(2)
        self.click_enter(self.input_project_name)

    def find_clicker_to_project_list(self):
        self.clicker_to_project_list = self._driver.find_element(*self.PROJECT_LIST_BUTTON)


    def find_project_name(self):
        self.find_project_name = self._driver.find_element(*self.PROJECT_NAME)

    def find_project(self):
        self.find_clicker_to_project_list()
        time.sleep(2)
        self.clicker_button(self.clicker_to_project_list)
        time.sleep(2)
        self.find_project_name()

    def find_project_to_delete(self):
        self.project_to_delete = self._driver.find_element(*self.FIND_TASK_TO_DELETE)

    def find_more_action_clicker(self, task):
        self.more_action_clicker = self._driver.find_element(By.XPATH, f"//div[./a[./div[./span[contains(text(),'{task}')]]]]//button[@aria-label='More project actions']")

    def find_delete_requste(self):
        self.delete_requeste = self._driver.find_element(By.XPATH, "//button[./div[contains(text(),'Delete')]]")

    def find_confrmation_delete_requste(self):
        self.confirm_delete_requeste = self._driver.find_element(By.XPATH, "//button[./span[contains(text(),'Delete')]]")

    def actions_perform(self, task_input):
        actions = ActionChains(self._driver)
        actions.move_to_element(task_input).perform()

    def delete_task(self, task_name):
        # self.find_clicker_to_project_list()
        # time.sleep(2)
        # self.clicker_button(self.clicker_to_project_list)
        # time.sleep(2)
        # self.find_project_to_delete()
        # self.actions_perform(self.project_to_delete)
        # time.sleep(2)
        self.find_more_action_clicker(task_name)
        time.sleep(2)
        self.action_prform_hover_over(self.more_action_clicker)
        time.sleep(2)
        self.clicker_button(self.more_action_clicker)
        time.sleep(2)
        self.find_delete_requste()
        time.sleep(2)
        self.clicker_button(self.delete_requeste)
        time.sleep(2)
        self.find_confrmation_delete_requste()
        time.sleep(5)
        self.clicker_button(self.confirm_delete_requeste)










