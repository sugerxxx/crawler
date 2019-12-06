# -*- coding: UTF-8 -*-
'''
Created on 2019 10�� 31��

@author: surface
'''

import requests
import time
from PyQt5.QtCore import QObject
from bs4 import BeautifulSoup
from urllib import parse,request
import shutil
import os
import random
import ssl


class URL(object):
    
    #login POST
# _login_sAction: MOBIL_LOGIN
# _login_user_name: hucy1129@tpl.cntaiping.com@union
# Proxy-Connection: close
# _login_encrypt_password: 842fde86516867320fbd064cbb8a879dab714d8067259799f8fa6c541be99230a2e10db89c07379740cebd57010adbf38c1c8bda205aa7088920a6d2b0169424ebb34c3676427dd3546cbfc11849105e18ed3383c6b4209ad928f757f8f9078e1609ad1ac3c8207075a71c8d9acf8abcb4394bda1c76a7ac03c90bd0a3094807
# APP_TYPE: 1241
# DEVICE_TYPE: 1
# DEVICE_CODE: 342A015A-65F4-462D-BA7E-50F942ACCFAE
# GEO_XY: 31.181880,121.455303
# INS_TYPE: LOGIN_INS
# RELEASE_CODE: 2.2.2
# X-Tingyun-Id: aK-pgll8fq8;c=2;r=492150800

    
    login_dict = {"_login_sAction": "MOBIL_LOGIN",
#"_login_user_name": "hucy1129@tpl.cntaiping.com@union",
#"Proxy-Connection": "close",
"_login_encrypt_password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"APP_TYPE": "1241",
"DEVICE_TYPE": "1",
"DEVICE_CODE": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"GEO_XY": "31.181880,121.455303",
"INS_TYPE": "LOGIN_INS",
"RELEASE_CODE": "2.2.2"
#"X-Tingyun-Id": "aK-pgll8fq8;c=2;r=492150800"
    
    }
    
    get_lastversion_txt = '0x63'+'0x01'+ '0x00'+ '0x6D' +'0x00'+ '0x05' 
    get_lastversion_dict = {"getLastVersionId": "2.2.2"
                               }
    '''
    
    login_dict = {
"_login_user_name": "hucy1129@tpl.cntaiping.com@union"
    }
    '''
    
    
    login_headers = {
        "Host": "emall.life.cntaiping.com",
        "User-Agent": "太平产品通 2.2.2 rv:1.0 (iPhone; iOS 12.0; zh_CN)" .encode("utf-8"),
                     "Accept-Encoding": "gzip",
                     #"Content-Type": "text/xml"
                     "Content-Type":"text/html; charset=utf-8",
                     "_login_sAction": "MOBIL_LOGIN",
"_login_user_name": "hucy1129@tpl.cntaiping.com@union",
#"Proxy-Connection": "close",
"_login_encrypt_password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"APP_TYPE": "1241",
"DEVICE_TYPE": "1",
"DEVICE_CODE": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"GEO_XY": "31.181880,121.455303",
"INS_TYPE": "LOGIN_INS",
"RELEASE_CODE": "2.2.2"
#"X-Tingyun-Id": "aK-pgll8fq8;c=2;r=492150800"
                     }
    
    get_lastversion_headers = {#"getLastVersionId": "2.2.2",
                               "INS_TYPE": "HEART_THROB",
                               "Content-Type":"text/xml",
                               "Accept-Encoding": "gzip",
                               "Proxy-Connection": "close",
                               "User-Agent": "太平产品通 2.2.2 rv:1.0 (iPhone; iOS 12.0; zh_CN)" .encode("utf-8")
                               }
    login_url = "https://emall.life.cntaiping.com/mobile/servlet/com.cntaiping.intserv.mservice.auth.login.MLoginServiceImpl"

    
    
    query_product_dict = {
#         Host: emall.life.cntaiping.com
# userId: 154037544
# Cookie: MOBILE_JS=yCcfsTPRCJmaCNIQrxr2OVBnuzbgs6BQdB7JxGNgmFknz3uPL1yz!812958756; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e1bc5c8e61ec-04831e5cda0ea7-5f02607b-250125-16e1bc5c8e7756%22%2C%22%24device_id%22%3A%2216e1bc5c8e61ec-04831e5cda0ea7-5f02607b-250125-16e1bc5c8e7756%22%2C%22props%22%3A%7B%7D%7D
# User-Agent: 太平产品通 2.2.2 rv:1.0 (iPhone; iOS 12.0; zh_CN)
# Proxy-Connection: close
# GEO_XY: 31.181880,121.455303
# X-Tingyun-Id: aK-pgll8fq8;c=2;r=186102584
# INS_TYPE: SIGHTSEER
# _login_user_name: hucy1129@tpl.cntaiping.com@union
# Content-Length: 641
# INTSERV_TOKEN: 
# DEVICE_CODE: 342A015A-65F4-462D-BA7E-50F942ACCFAE
# Connection: close
# PLANT_ID: 151
# _login_encrypt_password: 842fde86516867320fbd064cbb8a879dab714d8067259799f8fa6c541be99230a2e10db89c07379740cebd57010adbf38c1c8bda205aa7088920a6d2b0169424ebb34c3676427dd3546cbfc11849105e18ed3383c6b4209ad928f757f8f9078e1609ad1ac3c8207075a71c8d9acf8abcb4394bda1c76a7ac03c90bd0a3094807
# APP_TYPE: 1241
# Content-Type: text/xml
# Accept-Encoding: gzip
# DEVICE_TYPE: 1
# RELEASE_CODE: 2.2.2
}
    query_product_url = "https://emall.life.cntaiping.com/mobile/servlet/mhessian/com.cntaiping.intserv.coverage.product.ProductInfoService"
    
    
class ParseTool(object):
    
    @classmethod
    def hex_to_str(cls,b):
        s = ''
        for i in b:
            s += '{0:0>2}'.format(str(hex(i))[2:])
        return s
    
    @classmethod
    def find_url_from_response(cls,content,str):
        url = ""
        html_text_lines = content.decode().split('\r\n')
        for line in html_text_lines:
            #print(line,len(line),type(line))
            if str in line:
                str_beg_pos = line.find(str)
                str_end_pos = line[str_beg_pos:].find("\"")
                #print(line[str_beg_pos:],str_beg_pos,str_beg_pos + str_end_pos)
                url = line[str_beg_pos:str_beg_pos + str_end_pos]
                #url = line[line.find("/kbs"):line.find(" target")-1]
        return url    
            
    @classmethod           
    def find_url_from_response2(cls,content,str):    
        soup = BeautifulSoup(content,"lxml")
        a_list = soup.find_all ("a")
        for a in a_list:
            if str in a["href"]:
                return a["href"]
        
        return ""
        
    
    @classmethod
    def downloading_file(cls,session,url_path,file_name):
        
        print("downloading..."  , url_path ,"to", file_name)
        
        #response= cls.session.get("http://10.21.0.2/kbs/upload/down-cdn/78eb2bba-71f2-4194-b71e-bf3b2cf6a284/0?dn=0")
        file_response = session.get(url_path )
        #print(file_response.headers)
        #print(response.content)
        f = open(file_name, "wb")
        f.write(file_response.content)
        f.close()
        return
    
    @classmethod
    def save_soup(cls,soup,file_name):
        print("Saving "+ file_name)
        content_file = open(file_name,'a',encoding='utf-8')
        print(soup.prettify(), file = content_file)
        content_file.close() 

class APITool(QObject):
    
    session = requests.session()
    
    
#     Cookie: MOBILE_JS=yCcfsTPRCJmaCNIQrxr2OVBnuzbgs6BQdB7JxGNgmFknz3uPL1yz!812958756; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e1bc5c8e61ec-04831e5cda0ea7-5f02607b-250125-16e1bc5c8e7756%22%2C%22%24device_id%22%3A%2216e1bc5c8e61ec-04831e5cda0ea7-5f02607b-250125-16e1bc5c8e7756%22%2C%22props%22%3A%7B%7D%7D
# X-Tingyun-Id: aK-pgll8fq8;c=2;r=492150800

  
    
    @classmethod
    def login_cpt(cls):
        print("Step: Login...")
        print("Cookies: ", cls.session.cookies)
        print(URL.get_lastversion_txt,ParseTool.hex_to_str(URL.get_lastversion_txt))
        input()
        sensorsdata2015jssdkcross="%7B%22distinct_id%22%3A%2216e1bc5c8e61ec-04831e5cda0ea7-5f02607b-250125-16e1bc5c8e7756%22%2C%22%24device_id%22%3A%2216e1bc5c8e61ec-04831e5cda0ea7-5f02607b-250125-16e1bc5c8e7756%22%2C%22props%22%3A%7B%7D%7D"
        cls.session.cookies.set("sensorsdata2015jssdkcross", sensorsdata2015jssdkcross)
        
        #ssl._create_default_https_context = ssl._create_unverified_context 
        #response = cls.session.post(URL.login_url,URL.login_dict , headers=URL.login_headers, verify=False)
        
        response = cls.session.post(URL.login_url , URL.get_lastversion_txt, headers=URL.get_lastversion_headers, verify=False)
        #response = cls.session.post(URL.login_url , headers=URL.login_headers, verify=False)
        
        print(response.headers)
        print(response.content)
        
        print("Cookies: ", cls.session.cookies)
        
        print("Logging Step complete!")
        print("")
        

    
   

if __name__ == '__main__':

    APITool.login_cpt()


