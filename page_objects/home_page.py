from selenium.webdriver.common.by import By


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver

    #   reusable getters for getting page elements. Could be enhanced by conditional waits to reduce flakiness
    def __get_header(self):
        return self.driver.find_element(By.CLASS_NAME, "dashboard-header")

    def __get_full_name(self):
        return self.driver.find_element(By.CLASS_NAME, "full-name")

    def __get_account_type(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".account-type-upgrade-btn-container .body-text")

    def __get_expiry_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".renewal-expiry-heading + .body-text")

    def __get_show_token_icon(self):
        return self.driver.find_element(By.XPATH, "//*[@data-testid='api-token-field-button']")

    def __get_api_token_element(self):
        return self.driver.find_element(By.CLASS_NAME, "component--ApiTokenField")

    #   public methods for interaction with page elements
    def get_header_text(self):
        return self.__get_header().text

    def get_user_full_name(self):
        return self.__get_full_name().text

    def get_account_type(self):
        return self.__get_account_type().text

    def get_expiry_date(self):
        return self.__get_expiry_element().text

    def click_on_show_token(self):
        self.__get_show_token_icon().click()

    def get_api_token(self):
        return self.__get_api_token_element().get_attribute('value')
