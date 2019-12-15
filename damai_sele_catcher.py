# -*- coding: UTF-8 -*-
'''
Created on 2019��12��3��

@author: pantherfire
'''


from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import time
# ���� WebDriver ����ָ��ʹ��chrome���������

desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出


option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
#brower = webdriver.Chrome(options=option)
#brower.get('file:///C:/Users/Administrator/Desktop/js.html')

wd = webdriver.Chrome(options=option)
wd.implicitly_wait(10)
wd.maximize_window()
#wd.get('file:///C:/Users/panth/Downloads/chromedriver_win32/js.html')
#input()
wd.get("https://www.damai.cn/?spm=a2oeg.home.top.dhome.176723e1XwFz3i")
#wd.get('https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F')
time.sleep(1)
wd.find_element_by_xpath("//span[@class='span-box-header span-user']").click()
time.sleep(1)

#wd.switch_to.frame('alibaba-login-box')
input()
timer1 = time.time()
'''
wd.find_element_by_id('fm-login-id').send_keys("13764288196")  

wd.find_element_by_id('fm-login-password').click()
time.sleep(2)
wd.find_element_by_id('fm-login-password').send_keys("Um111111")  

wd.find_element_by_xpath("//button[text()='登录']").click()
'''
#print(wd.get_cookies())
#wd.get("https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_0.492a23e1L4m6MG&id=609134671437")
wd.get("https://detail.damai.cn/item.htm?id=609134671437")
wd.find_element_by_xpath("//div[text()='看台680元']").click()
wd.find_element_by_xpath("//div[@class='buybtn']").click()
#wd.find_element_by_xpath("//span[text()='杨佳楣']/preceding-sibling::span").click()

#wd.execute_script(myjs)
dr = wd.find_element_by_xpath("//span[text()='胡超晔']/preceding-sibling::span//input");
#wd.find_element_by_xpath("//span[text()='胡超晔']/preceding-sibling::span//input").click()
#print(dr.get_attribute('outerHTML'))
ActionChains(wd).click(dr).perform()

wd.find_element_by_xpath("//button[@class='next-btn next-btn-normal next-btn-medium'][text()='同意以上协议并提交订单']").click()
timer2 = time.time()
print(timer2-timer1)
#input()

#wd.find_element_by_class_name('fm-button fm-submit password-login').click()

