from base.LoginBase import LoginBase


class LoginPage(LoginBase):
    def login_input_value(self, driver, input_placeholder, input_value):
        # "登录页输入值
        # "
        input_xpath = self.login_input(input_placeholder)
        return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def click_login(self, driver, button_name):
        "点击登录"
        button_xpath = self.login_button(button_name)
        return driver.find_element_by_xpath(button_xpath).click()
