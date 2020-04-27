import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from common.element_dta_utils import ElementdataUtils
from common.element_data_utils_yaml import ElementdataUtilsYaml



class MyzonePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        login_page = LoginPage(driver)
        login_page.open_url('http://106.53.50.202:8999/zentao2/www/my-managecontacts.html')
        login_page.input_username('hanruqing')
        login_page.input_password('Aa234567')
        login_page.click_login()
        # self.calendar_href={'element_name':'日程链接',
        #                 'locator_type':'xpath',
        #                 'locator_value':'//li[@data-id="calendar"]',
        #                 'timeout':5
        #                   }
        # self.manageContacts_href = {'element_name': '联系人链接',
        #                       'locator_type': 'xpath',
        #                       'locator_value': '//li[@data-id="manageContacts"]',
        #                       'timeout': 5
        #                       }
        # self.newList_inputbox = {'element_name': '列表名称输入框',
        #                             'locator_type': 'xpath',
        #                             'locator_value': '//input[@id="newList"]',
        #                             'timeout': 5
        #                             }
        # self.users_chosen_combobox = {'element_name': '用户选择下拉框',
        #                             'locator_type': 'xpath',
        #                             'locator_value': '//div[@id="users_chosen"]',
        #                             'timeout': 5
        #                             }
        # self.choose_users_box = {'element_name': '选择用户',
        #                               'locator_type': 'xpath',
        #                               'locator_value': '//li[@title="陈江林"]',
        #                               'timeout': 5
        #                               }
        # self.save_button = {'element_name': '保存列表按钮',
        #                          'locator_type': 'xpath',
        #                          'locator_value': '//button[@id="submit"]',
        #                          'timeout': 5
        #                          }
        # self.delete_button = {'element_name': '删除列表按钮',
        #                     'locator_type': 'xpath',
        #                     'locator_value': '//a[@class="btn btn-danger btn-wide"]',
        #                     'timeout': 5
        #                     }
        # self.changepasswd_href={'element_name':'修改密码链接',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//li[@data-id="changePassword"]',
        #                         'timeout':5}
        # self.originalpasswd_inputbox={'element_name':'原始密码输入框',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@id="originalPassword"]',
        #                         'timeout':5}
        # self.newpasswd_inputbox1 = {'element_name': '新密码输入框1',
        #                                 'locator_type': 'xpath',
        #                                 'locator_value': '//input[@id="password1"]',
        #                                 'timeout': 5}
        # self.newpasswd_inputbox2 = {'element_name': '新密码输入框2',
        #                             'locator_type': 'xpath',
        #                             'locator_value': '//input[@id="password2"]',
        #                             'timeout': 5}
        # self.savepasswd_button = {'element_name': '密码保存按钮',
        #                             'locator_type': 'xpath',
        #                             'locator_value': '//button[@id="submit"]',
        #                             'timeout': 5}
        elements=ElementdataUtils('myzone_page').get_element_info()
        # elements=ElementdataUtilsYaml().get_element_info_by_yaml()
        self.manageContacts_href=elements['manageContacts_href']
        self.newList_inputbox=elements['newList_inputbox']
        self.users_chosen_combobox=elements['users_chosen_combobox']
        self.choose_users_box=elements['choose_users_box']
        self.save_button=elements['save_button']
        self.changepasswd_href=elements['changepasswd_href']
        self.originalpasswd_inputbox=elements['originalpasswd_inputbox']
        self.newpasswd_inputbox1=elements['newpasswd_inputbox1']
        self.newpasswd_inputbox2=elements['newpasswd_inputbox2']
        self.savepasswd_button=elements['savepasswd_button']


    # def click_calendar(self):
    #     self.click(self.calendar_href)
    def click_manageContacts(self):
        self.click(self.manageContacts_href)

    def add_newlist(self,newlist):
        self.input(self.newList_inputbox,newlist)
        self.click(self.users_chosen_combobox)
        self.click(self.choose_users_box)
        self.click(self.save_button)
        time.sleep(3)
        self.refresh()
        # self.click(self.delete_button)

    def change_password(self,originalpasswd,newpasswd1,newpasswd2):
        self.click(self.changepasswd_href)
        self.driver.switch_to.frame('iframe-triggerModal')
        self.input(self.originalpasswd_inputbox,originalpasswd)
        time.sleep(2)
        self.input(self.newpasswd_inputbox1,newpasswd1)
        time.sleep(2)
        self.input(self.newpasswd_inputbox2,newpasswd2)
        time.sleep(2)
        self.click(self.savepasswd_button)



if __name__=="__main__":
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, '../webdriver/geckodriver')
    driver=webdriver.Firefox(executable_path=driver_path)
    myzone_page=MyzonePage(driver)
    # myzone_page.click_calendar()
    myzone_page.click_manageContacts()
    myzone_page.add_newlist('列表1')
    myzone_page.change_password('Aa234567','Aa123456','Aa123456')

