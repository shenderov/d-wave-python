from tools.driver_manager import WebDriverManager
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from time import sleep
import unittest

#   These parameters should be set on env/project level for a static user or as part of test data
#   generation for disposable test data
username = "konstantin.shenderov@d-wave.com"
password = "Password!"
url = "https://cloud.dwavesys.com/leap/login/"
#   User full name should be part of test data generation
user_full_name = "Konstantin Shenderov"
#   expiry date should be calculated for a generated test user
expiry_date = "February 17, 2023 (UTC)"
#   should be set as part of test data generation
account_type = "Trial Plan"


class HomePageTest(WebDriverManager):

    def test_home_page(self):
        #   open URL and login into dashboard
        self.driver.get(url)
        self.driver.set_page_load_timeout(30)

        login_page = LoginPage(self.driver)
        web_page_title = "D-Wave Leap Log In | D-Wave Leap"

        self.assertEqual(self.driver.title, web_page_title, "Login page was not loaded properly")

        login_page.set_username("shenderov.k@gmail.com")
        login_page.set_password(password)
        login_page.click_on_login_button()

        home_page = HomePage(self.driver)
        #   Verify dashboard title
        self.assertEqual(home_page.get_header_text(), "Dashboard")
        #   Verify full username
        self.assertEqual(home_page.get_user_full_name(), user_full_name)
        #   Verify account type
        self.assertEqual(home_page.get_account_type(), account_type)
        #   Verify expiry date
        self.assertEqual(home_page.get_expiry_date(), expiry_date)
        #   click on show token icon and verify token value is not empty
        home_page.click_on_show_token()
        self.assertTrue(home_page.get_api_token())

        sleep(10)


if __name__ == '__main__':
    unittest.main()
