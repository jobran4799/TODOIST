import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from os.path import dirname as up

class BrowserWrapper:

    def __init__(self):
        self.driver = None
        cur_dir = up(up(up(os.path.abspath(__file__))))
        config_location = os.path.join(cur_dir, 'config.json')
        with open(config_location) as f:
            self.data = json.load(f)

    def get_driver(self, brawser):
        if self.data["headless"]:
            self.headless_get_driver(brawser)
            url = self.data["url"]
            self.driver.get(url)
            time.sleep(4)
            return self.driver
        elif self.data["grid"]:
            if brawser.lower() == 'chrome':
                options = webdriver.ChromeOptions()
            elif brawser.lower() == 'firefox':
                options = webdriver.FirefoxOptions()
            elif brawser.lower() == 'edge':
                options = webdriver.EdgeOptions()
            platform_name = self.data["platform"]
            options.add_argument(f'--platformName={platform_name}')
            self.driver = webdriver.Remote(command_executor=self.data["hub"], options=options)
        else:
            if brawser.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif brawser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif brawser.lower() == 'edge':
                self.driver = webdriver.Edge()
        url = self.data["url"]
        self.driver.get(url)
        time.sleep(4)
        return self.driver

    def headless_get_driver(self, brawser):
        option = Options()
        option.add_argument('--headless')
        option.add_argument('--no--sandbox')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--window-size=1920x1080')
        if self.data["grid"]:
            if brawser.lower() == 'chrome':
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                options.add_argument('--no--sandbox')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument('--window-size=1920x1080')
            elif brawser.lower() == 'firefox':
                options = webdriver.FirefoxOptions()
                options.add_argument('--headless')
                options.add_argument('--no--sandbox')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument('--window-size=1920x1080')
            elif brawser.lower() == 'edge':
                options = webdriver.EdgeOptions()
                options.add_argument('--headless')
                options.add_argument('--no--sandbox')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument('--window-size=1920x1080')
            platform_name = self.data["platform"]
            options.add_argument(f'--platformName={platform_name}')
            self.driver = webdriver.Remote(command_executor=self.data["hub"], options=options)
        else:
            if brawser.lower() == 'chrome':
                self.driver = webdriver.Chrome(options=option)
            elif brawser.lower() == 'firefox':
                self.driver = webdriver.Firefox(options=option)
            elif brawser.lower() == 'edge':
                self.driver = webdriver.Edge(options=option)




    def close_browser(self):
        if self.driver:
            self.driver.close()


