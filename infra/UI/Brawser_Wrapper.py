import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    with open('../../Config_Manegre/config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run


class BrowserWrapper:

    def __init__(self):
        self.driver = None

    def get_driver(self, brawser):
        if data["headless"]:
            option = Options()
            option.add_argument('--headless')
        if data["grid"]:
            if brawser.lower() == 'chrome':
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
            elif brawser.lower() == 'firefox':
                options = webdriver.FirefoxOptions()
                options.add_argument('--headless')
            elif brawser.lower() == 'edge':
                options = webdriver.EdgeOptions()
                options.add_argument('--headless')
            platform_name = data["platform"]
            options.add_argument(f'--platformName={platform_name}')
            self.driver = webdriver.Remote(command_executor=data["hub"], options=options)
        else:
            if brawser.lower() == 'chrome':
                self.driver = webdriver.Chrome(options=option)
            elif brawser.lower() == 'firefox':
                self.driver = webdriver.Firefox(options=option)
            elif brawser.lower() == 'edge':
                self.driver = webdriver.Edge(options=option)
        url = data["url"]
        self.driver.get(url)
        time.sleep(4)
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.close()


