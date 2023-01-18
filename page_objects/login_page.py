from selenium.webdriver.common.by import By


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    #   reusable getters for getting page elements. Could be enhanced by conditional waits to reduce flakiness
    def __get_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h1.title")

    def __get_username_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='username']")

    def __get_password_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='password']")

    def __get_login_button(self):
        return self.driver.find_element(By.ID, "loginFormSubmit")

    def __get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "login-error")

    #   public methods for interaction with page elements
    def get_title_text(self):
        return self.__get_title().text

    def set_username(self, username):
        self.__get_username_input().send_keys(username)

    def set_password(self, password):
        self.__get_password_input().send_keys(password)

    def click_on_login_button(self):
        self.__get_login_button().click()

    def get_error_message_text(self):
        return self.__get_error_message().text
