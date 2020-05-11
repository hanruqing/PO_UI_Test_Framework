import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
# from common.element_dta_utils import ElementdataUtils
from common.element_data_utils_yaml import ElementdataUtilsYaml
from common.browsers import Browser


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.username_inputbox={'element_name':'用户名输入框',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@id="account"]',
        #                         'timeout':5}
        # self.password_inputbox={'element_name':'密码输入框',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@name="password"]',
        #                         'timeout':5}
        # self.login_button={'element_name':'登录按钮',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//button[@id="submit"]',
        #                         'timeout':2}
        # elements = ElementdataUtils('login_page').get_element_info()
        # self.username_inputbox=elements['username_inputbox']
        # self.password_inputbox=elements['password_inputbox']
        # self.login_button=elements['login_button']
        elements=ElementdataUtilsYaml().get_element_info_by_yaml()
        self.username_inputbox=elements['username_inputbox']
        self.password_inputbox=elements['password_inputbox']
        self.login_button=elements['login_button']





    def input_username(self,username): #方法==》控件的操作
        self.input(self.username_inputbox,username)
        # logger.info('用户名输入框输入：'+str(username))

    def input_password(self,password):
        self.input(self.password_inputbox,password)
        # logger.info('密码输入框输入：' + str(password))
    def click_login(self):
        self.click(self.login_button)
        logger.info('点击登录')



if __name__=="__main__":
    driver=Browser().get_driver()
    #浏览器封装，替代以下语句
    # current_path = os.path.dirname(__file__)
    # driver_path = os.path.join(current_path, '../webdriver/geckodriver')
    # driver=webdriver.Firefox(executable_path=driver_path)
    login_page=LoginPage(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao2/www/user-login-L3plbnRhbzIvd3d3L215Lmh0bWw=.html')
    login_page.input_username('hanruqing')
    login_page.input_password('Aa234567')
    login_page.click_login()

