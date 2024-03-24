import time
from selenium.webdriver import Keys, ActionChains
from infra.UI.Base_Page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class MainPage(BasePage):
    USER_NAME = (By.XPATH, "//span[text() = 'Beyonddev']")
    def __init__(self, driver):
        super().__init__(driver)
        # self.init()

    def init(self):
        self.user_name = self._driver.find_element(*self.USER_NAME)


    def username_is_displayed(self):
        return self.user_name.is_displayed()


    def fill_input(self, element, text):
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(element)).send_keys(text)

    def click_enter(self, element):
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(element)).send_keys(Keys.ENTER)

    def clicker_button(self, element):
        element.click()

    def action_perform_hover_over(self, element):
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def find_task_inputs_to_add_task(self):
        self.task_input = self._driver.find_element(By.XPATH, "//button[contains(text(),'Add task')]")

    def find_add_task_name_to_add_task(self):
        self.add_task_name = self._driver.find_element(By.XPATH, "//div[contains(@aria-label,'Task name')]//p[@data-placeholder='Task name']")

    def create_task(self, text_task_name):
        task_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Add task')]"))
        )
        task_input.click()

        # Wait for the add task name input field to be visible
        self.find_add_task_name_to_add_task()
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.add_task_name))
        self.add_task_name.send_keys(text_task_name)

        # Perform action only when the input field is ready
        self.add_task_name.send_keys(Keys.ENTER)


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

        # Hover over the task element
        self.action_perform_hover_over(self.task_delete_input)

        # Wait for the menu clicker button to be clickable
        self.find_more_menu_clicker(task_name)
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.menu_clicker))

        # Click the menu clicker button
        self.clicker_button(self.menu_clicker)

        # Wait for the delete request button to be clickable
        self.find_delete_requste()
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.delete_requeste))

        # Click the delete request button
        self.clicker_button(self.delete_requeste)

        # Wait for the confirmation delete request button to be clickable
        self.find_confrmation_delete_requste()
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.confirm_delete_requeste))

        # Click the confirmation delete request button
        self.clicker_button(self.confirm_delete_requeste)


    def find_task_inputs_to_edit_task(self, task_name):
        self.inputs_to_edit_task = self._driver.find_element(By.XPATH,  f"//div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]")


    def find_add_descrption(self, task_name):
        self.add_descrption = self._driver.find_element(By.XPATH,  f"//div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]//div[contains(@class,'task-overview-description-placeholder')]")

    def find_confirm_edit(self):
        self.confirm_edit = self._driver.find_element(By.XPATH,  "//div[contains(@aria-label,'Description')]")

    def clicker_button_with_retry(self, element):
        retry_attempts = 3
        for _ in range(retry_attempts):
            try:
                element.click()
                return  # Click successful, exit the loop
            except Exception as e:
                print(f"Click failed: {e}")
                time.sleep(1)  # Wait for 1 second before retrying
        print("Failed to click the element after multiple attempts")

    def edit_task(self, text_edit):
        # Click on the task edit
        self.find_task_inputs_to_edit_task(text_edit)
        self.clicker_button_with_retry(self.inputs_to_edit_task)

        # Wait for the add description element to appear
        add_description_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'task-overview-description-placeholder')]"))
        )

        # Click on the add description element
        self.clicker_button_with_retry(add_description_element)

        # Send keys to the confirm edit element
        self.find_confirm_edit()  # Assuming confirm edit element is constant after clicking on add description
        confirm_edit_element = self.confirm_edit
        confirm_edit_element.send_keys(text_edit)

        # Click Enter to confirm the edit
        self.click_enter(confirm_edit_element)


    def find_menu_priority(self, task_name):
        xpath = f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]//button[contains(@data-testid,'more_menu')]"
        self.menu_priority = self._driver.find_element(By.XPATH, xpath)

    def find_task_for_priority(self, task_name):
        xpath = f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]"
        self.task_for_priority = self._driver.find_element(By.XPATH, xpath)

    def find_choose_num_of_priority(self, priority_level):
        xpath = f"//button[contains(@aria-label,'Priority {priority_level}')]"
        self.confirm_edit_priority = self._driver.find_element(By.XPATH, xpath)

    def priority_task(self, task_name, priority_level):
        self.find_task_for_priority(task_name)
        self.action_perform_hover_over(self.task_for_priority)

        self.find_menu_priority(task_name)
        # Wait for the menu to appear
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.menu_priority.xpath)))

        # Find the menu button


        # Click on the menu button
        self.clicker_button_with_retry(self.menu_priority)

        self.find_choose_num_of_priority(priority_level)
        # Wait for the priority option to appear
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.confirm_edit_priority.xpath)))

        # Find and click on the priority option
        self.clicker_button(self.confirm_edit_priority)

    def find_click_on_due_date(self, task_name):
        self.click_on_due_date = self._driver.find_element(By.XPATH, f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]//button[contains(@aria-label, 'Due date')]")

    def find_choose_date(self):
        self.choose_date = self._driver.find_element(By.XPATH, "//button[contains(@aria-label,'2024-04-05')]")


    def set_due_date_task(self, task_name):
        self.find_click_on_due_date(task_name)
        click_on_due_date_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//li[./div[./div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]]]//button[contains(@aria-label, 'Due date')]"))
        )
        click_on_due_date_button.click()

        self.find_choose_date()
        choose_date_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label,'2024-04-05')]"))
        )
        choose_date_button.click()



    def click_completed_task(self, task_name):
        self.completed_task = self._driver.find_element(By.XPATH,  f"//div[./div[./div[./div[./div[./div[contains(text(),'{task_name}')]]]]]]//button[contains(@class,'task_checkbox')]")
        self.completed_task.click()
















