import time
from selenium.webdriver import Keys, ActionChains
from infra.UI.Base_Page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    USER_NAME = (By.XPATH, "//span[text() = 'Beyonddev']")

    # TASK_INPUT = (By.XPATH, "//button[@class='vZhNClH _8313bd46 f169a390 _5e45d59f fb8d74bb _8c75067a']")
    #               # "//div[@class='fb8d74bb _14423c92 _297575f4 c4a9b3ab _5f8879d9']//button [@tabindex='0']")
    # ADD_TASK_NAME = (By.XPATH,
    #                  "//div[@class = 'UjpFDa7 no-focus-marker XOgsZVX']//p[@class='is-empty is-editor-empty']")
    #
    # DELETION_INPUT = (By.XPATH, "//div[@data-index='0']")
    # MORE_MENU = (By.XPATH, "//div/div/button[@data-testid='more_menu']")
    # DELETE_REQUST = (By.XPATH, "// div[ @class ='a83bd4e0 a8d37c6e _2f303ac3 fb8d74bb _211eebc7' and text()='Delete']")
    # CONFIRMATION_DELETE = (By.XPATH, "//form/footer/div/button[./span[contains(text(),'Delete')]]")
    #
    # TASK_TO_EDIT = (By.XPATH,
    # "//div[contains(@class, '_560c1e08')]/div[contains(@class, 'task_content') and text()='test task editing']")
    # CLIC_ON_EDIT = (By.XPATH,
    # "//div[@class='YjMLlDP task_list_item__actions task_list_item__actions--active']/button[@aria-label='Edit']")
    # ADD_DESCRPTION = (By.XPATH, "//p[@data-placeholder='Description' and contains(@class, 'is-empty') and contains(@class, 'is-editor-empty')]/br[@class='ProseMirror-trailingBreak']")
    # CONFIRM_EDIT = (By.XPATH, "//button[@data-testid='task-editor-submit-button']")
    #
    # FIND_TASK_NO_PRIORITY = (By.XPATH, "//div[contains(@class, '_560c1e08')]/div[contains(@class, 'task_content') and text()='task to change priority']")
    # MENU_FOR_PRIORITY = (By.XPATH, "//div/div/button[@data-testid='more_menu']")
    # NUM_PRIORITY = (By.XPATH, "//div[@class='fb8d74bb _14423c92 c7813d79 _6a4f69f7 _5f8879d9 _43e5f8e9']/button[@aria-label='Priority 2']")
    #
    # FIND_SET_DUE_DATE = (By.XPATH, "//div[@class='task_content' and text()='task set due data']")
    # CLICK_ON_DUE_DATE = (By.XPATH, "//div[contains(@class, 'task_list_item__content') and .//div[text()='task set due data']]//button[@class='due_date_controls']")
    # CHOOSE_DATE = (By.XPATH, "//button[@aria-label='2024-04-04']")
    #
    # FIND_COMPLETE_TASK = (By.XPATH, "//div[contains(@class, '_560c1e08')]/div[contains(@class, 'task_content') and text()='test Completed task']")
    #
    # FIND_MY_PROJECTS = (By.XPATH, "//button[@aria-label='My projects menu']")
    # FIND_CLICKER_TO_ADD_PROJECT = (By.XPATH, "//div[@class='a83bd4e0 e214ff2e fb8d74bb' and text()='Add project']")
    # INPUT_TEXT_ADD_PROJECT = (By.XPATH, "//input[@id='edit_project_modal_field_name']")
    # ADD_PROJECT_TO_FAVORITE = (By.XPATH, "//div[contains(@class, '_618235b7') and contains(@class, 'fb8d74bb') and contains(@class, '_18f74af9') and contains(@class, '_68aab614')]/input[@name='is_favorite']")
    #
    # PROJECT_LIST_BUTTON = (By.XPATH, "//div[contains(@class, 'qMjaCbb') and contains(@class, 'a83bd4e0') and contains(@class, '_7be5c531') and contains(@class, '_6a3e5ade') and contains(@class, '_2f303ac3') and contains(@class, 'fb8d74bb') and contains(@class, '_211eebc7') and text()='My Projects']")
    # PROJECT_NAME = (By.XPATH,
    #                 "//ul[@id='projects_list']//span[@class='X_3UwghUggmfmKrS8M8uwnLl4hgJenHE a83bd4e0 _2f303ac3 fb8d74bb _211eebc7' and text()='final project']/ancestor::div[@class='pMTLzg8']")

    def __init__(self, driver):
        super().__init__(driver)
        # self.init()

    def init(self):
        self.user_name = self._driver.find_element(*self.USER_NAME)


    def username_is_displayed(self):
        return self.user_name.is_displayed()

    def fill_input(self, task_input, task_TaskName):
        task_input.send_keys(task_TaskName)
        time.sleep(2)

    def click_enter(self, write_input):
        # WebDriverWait(self._driver, 10).until(
        #     EC.presence_of_element_located(write_input))
        write_input.send_keys(Keys.ENTER)


    def clicker_button(self, click):
        # WebDriverWait(self._driver, 10).until(
        #     EC.element_to_be_clickable(click))
        click.click()

    def action_prform_hover_over(self, hover_to_project):
        actions = ActionChains(self._driver)
        actions.move_to_element(hover_to_project).perform()



    def find_task_inputs_to_add_task(self):
        self.task_input = self._driver.find_element(By.XPATH, "//button[contains(text(),'Add task')]")

    def find_add_task_name_to_add_task(self):
        self.add_task_name = self._driver.find_element(By.XPATH, "//div[contains(@aria-label,'Task name')]//p[@data-placeholder='Task name']")

    def creat_task(self, text_task_name):
        self.find_task_inputs_to_add_task()
        time.sleep(2)
        self.clicker_button(self.task_input)
        time.sleep(2)
        self.find_add_task_name_to_add_task()
        time.sleep(2)
        self.fill_input(self.add_task_name, text_task_name)
        time.sleep(2)
        self.click_enter(self.add_task_name)

    def find_task_inputs_to_delete_task(self, task_name):
        self.task_delete_input = self._driver.find_element(By.XPATH,  f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]")

    def find_more_menu_clicker(self, task_name):
        self.menu_clicker = self._driver.find_element(By.XPATH,  f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]//button[contains(@data-testid,'more_menu')]")

    def find_delete_requste(self):
        self.delete_requeste = self._driver.find_element(By.XPATH, "//button[contains(@data-action-hint,'task-overflow-menu-delete')]")

    def find_confrmation_delete_requste(self):
        self.confirm_delete_requeste = self._driver.find_element(By.XPATH, "//button[contains(@data-autofocus,'true')]")

    def actions_perform(self, task_input):
        actions = ActionChains(self._driver)
        actions.move_to_element(task_input).perform()

    def delete_task(self, task_name):
        self.find_task_inputs_to_delete_task(task_name)
        self.action_prform_hover_over(self.task_delete_input)
        time.sleep(2)
        self.actions_perform(self.task_delete_input)
        time.sleep(2)
        self.find_more_menu_clicker(task_name)
        time.sleep(2)
        self.clicker_button(self.menu_clicker)
        time.sleep(2)
        self.find_delete_requste()
        time.sleep(2)
        self.clicker_button(self.delete_requeste)
        time.sleep(2)
        self.find_confrmation_delete_requste()
        time.sleep(2)
        self.clicker_button(self.confirm_delete_requeste)

    def find_task_inputs_to_edit_task(self, task_name):
        self.inputs_to_edit_task = self._driver.find_element(By.XPATH,  f"//div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]")

    # def find_click_on_edit(self):
    #     self.click_on_edit = self._driver.find_element(*self.CLIC_ON_EDIT)

    def find_add_descrption(self, task_name):
        self.add_descrption = self._driver.find_element(By.XPATH,  f"//div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]//div[contains(@class,'task-overview-description-placeholder')]")

    def find_confirm_edit(self):
        self.confirm_edit = self._driver.find_element(By.XPATH,  "//div[contains(@aria-label,'Description')]")

    def edit_task(self, text_edit):
        self.find_task_inputs_to_edit_task(text_edit)
        self.action_prform_hover_over(self.inputs_to_edit_task)
        # self.actions_perform(self.inputs_to_edit_task)
        # time.sleep(2)
        # self.find_click_on_edit()
        # time.sleep(2)
        self.clicker_button(self.inputs_to_edit_task)
        # time.sleep(2)
        self.find_add_descrption(text_edit)
        time.sleep(2)
        self.clicker_button(self.add_descrption)
        self.find_confirm_edit()
        time.sleep(2)
        self.confirm_edit.send_keys("text_edit")
        time.sleep(2)
        self.click_enter(self.confirm_edit)
        # self.find_confirm_edit()
        # time.sleep(2)
        # self.actions_perform(self.confirm_edit)
        # self.clicker_button(self.confirm_edit)


    def find_menu_priority(self, task_name):
        self.menu_priority = self._driver.find_element(By.XPATH,  f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]//button[contains(@data-testid,'more_menu')]")

    def find_task_for_priority(self, task_name):
         self.task_for_priority = self._driver.find_element(By.XPATH,  f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]")

    def find_choose_num_of_priority(self):
        self.confirm_edit_priority = self._driver.find_element(By.XPATH, "//button[contains(@aria-label,'Priority 3')]")

    def priority_task(self, task_name):
        self.find_task_for_priority(task_name)
        self.action_prform_hover_over(self.task_for_priority)
        time.sleep(2)
        self.find_menu_priority(task_name)
        time.sleep(2)
        # WebDriverWait(self._driver, 10).until(
        #     EC.element_to_be_clickable(self.task_for_priority))
        self.clicker_button(self.menu_priority)
        time.sleep(2)
        self.actions_perform(self.task_for_priority)
        self.find_choose_num_of_priority()
        time.sleep(2)
        self.clicker_button(self.confirm_edit_priority)

    def find_task_set_due_date(self, task_name):
        self.task_set_due_date = self._driver.find_element(By.XPATH, f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]")


    def find_click_on_due_date(self, task_name):
        self.click_on_due_date = self._driver.find_element(By.XPATH, f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]//button[contains(@aria-label, 'Due date')]")

    def find_choose_date(self):
        self.choose_date = self._driver.find_element(By.XPATH, "//button[contains(@aria-label,'2024-04-05')]")

    def set_due_date_task(self, task_name):
        self.find_task_set_due_date(task_name)
        self.action_prform_hover_over(self.task_set_due_date)
        # self.clicker_button(self.task_set_due_date)
        # self.actions_perform(self.task_set_due_date)
        # time.sleep(2)
        self.find_click_on_due_date(task_name)
        time.sleep(2)
        self.clicker_button(self.click_on_due_date)
        # time.sleep(2)
        self.find_choose_date()
        time.sleep(2)
        self.clicker_button(self.choose_date)

    # def find_task_complition(self):
    #     self.find_completed_task = self._driver.find_element(*self.FIND_COMPLETE_TASK)

    def click_completed_task(self, task_name):
        self.completed_task = self._driver.find_element(By.XPATH,  f"//div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]//button[contains(@class,'task_checkbox')]")
        self.completed_task.click()

    # def set_complation_task(self,task_name):
    #     self.find_task_complition()
    #     self.actions_perform(self.find_completed_task)
    #     time.sleep(2)
    #     self.find_click_completed(task_name)
    #     time.sleep(2)
    #     self.clicker_button(self.completed_task)















