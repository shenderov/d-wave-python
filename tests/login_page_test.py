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


class LoginPageTest(WebDriverManager):

    def test_login_page(self):
        #   open URL and wait until login page is loaded
        self.driver.get(url)
        self.driver.set_page_load_timeout(30)

        login_page = LoginPage(self.driver)

        web_page_title = "D-Wave Leap Log In | D-Wave Leap"
        login_form_title = "Leap In"

        #   verify page title and login page title
        self.assertEqual(self.driver.title, web_page_title, "Login page was not loaded properly")
        self.assertEqual(login_page.get_title_text(), login_form_title, "Login form title not equals to expected "
                                                                        "string")
        #   attempt to log in with wrong credentials and verify error message is present
        login_page.set_username("joe.doe3@company.com")
        login_page.set_password("Pa$$w0rd")
        login_page.click_on_login_button()

        self.assertTrue(login_page.get_error_message_text())

        #   login with correct credentials
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_on_login_button()

        home_page = HomePage(self.driver)

        #   verify home page is loaded by checking dashboard header is not empty
        #   this will fail now because the app requires TFA code to log in. It should be disabled for a test user
        self.assertTrue(home_page.get_header_text())

        sleep(10)


if __name__ == '__main__':
    unittest.main()
