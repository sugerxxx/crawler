# -*- coding: UTF-8 -*-
'''
Created on 2019��12��3��

@author: pantherfire
'''


from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
# ���� WebDriver ����ָ��ʹ��chrome���������



option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
#brower = webdriver.Chrome(options=option)
#brower.get('file:///C:/Users/Administrator/Desktop/js.html')

wd = webdriver.Chrome(r'C:\Users\panth\Downloads\chromedriver_win32\chromedriver.exe',options=option)
wd.implicitly_wait(10)
wd.maximize_window()
#wd.get('file:///C:/Users/panth/Downloads/chromedriver_win32/js.html')
#input()
wd.get("https://www.damai.cn/?spm=a2oeg.home.top.dhome.176723e1XwFz3i")
#wd.get('https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F')
time.sleep(2)
wd.find_element_by_xpath("//span[@class='span-box-header span-user']").click()
time.sleep(2)

wd.switch_to.frame('alibaba-login-box')
input()
'''
wd.find_element_by_id('fm-login-id').send_keys("13764288196")  

wd.find_element_by_id('fm-login-password').click()
time.sleep(2)
wd.find_element_by_id('fm-login-password').send_keys("Um111111")  

wd.find_element_by_xpath("//button[text()='登录']").click()
'''
print(wd.get_cookies())
#wd.find_element_by_class_name('fm-button fm-submit password-login').click()

