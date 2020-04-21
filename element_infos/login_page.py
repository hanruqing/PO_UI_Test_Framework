import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger

current_path=os.path.dirname(__file__)
driver_path=os.path.join(current_path,'../webdriver/geckodriver')

class LoginPage(object):
    def __init__(self):
        self.driver=webdriver.Firefox(executable_path=driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/biz/user-login-L2Jpei8=.html')
        self.username_inputbox=self.driver.find_element(By.XPATH, '//input[@id="account"]') #属性==》页面上的控件
        self.password_inputbox=self.driver.find_element(By.XPATH, '//input[@name="password"]')
        self.login_button=self.driver.find_element(By.XPATH, '//button[@id="submit"]')
        self.keeplogin_checkbox=None

    def input_username(self,username): #方法==》控件的操作
        self.username_inputbox.send_keys(username)
        logger.info('用户名输入框输入：'+str(username))

    def input_password(self,password):
        self.password_inputbox.send_keys(password)
        logger.info('密码输入框输入：' + str(password))
    def click_login(self):
        self.login_button.click()
        logger.info('点击登录')


if __name__=="__main__":
    login_page=LoginPage()
    login_page.input_username('admin')
    login_page.input_password('Aa123456')
    login_page.click_login()
