import unittest
from get_chrome_driver import GetChromeDriver
from selenium import webdriver


class WebDriverManager(unittest.TestCase):
    def setUp(self):
        print("Setting up the webdriver")
        self.get_driver = GetChromeDriver()
        self.get_driver.install()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            print("Closing the webdriver")
            self.driver.close()
            self.driver.quit()
