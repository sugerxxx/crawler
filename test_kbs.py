# -*- coding: UTF-8 -*-
'''
Created on 2019 10 9

@author: surface
'''

#from PyQt5.Qt import  *
import requests
from PyQt5.QtCore import QObject


class URL(object):
    
    #login POST
#     loginName: qianxt0929
#     postfix: @tpl.cntaiping.com
#     password: VHAxMjM0NTY=
#      Tp123456
    login_url = "http://10.21.0.2/kbs/login"
    
    cc_bottom_url = "http://10.21.0.2/kbs/home/cc-bottom"
    
    address_url = "http://10.21.0.2/kbs/home/portlet/ajax-list-address"
    
    full_text_search_url = "http://10.21.0.2/kbs/search?st=TYPE_FULLTEXT&q="

class APITool(QObject):
    session = requests.session()
    
    @classmethod
    def login_kbs(cls):
        data_dict = {'loginName': 'qianxt0929',
                        'postfix': '@tpl.cntaiping.com',
                        'password': 'VHAxMjM0NTY='}
        
        response = cls.session.post(URL.login_url,data_dict)

#         print(response.content)
#         print("")
#         print(response.json)
#         print("")

        print(cls.session.cookies)
        print("")

    
    @classmethod
    def cc_bottom(cls):

        
        response = cls.session.get(URL.cc_bottom_url)

        print(response.content)
        print("")
        print(response.content.decode())
        print("")
        print(response.json)
        print("")

        print(cls.session.cookies)
        print("")
        
    @classmethod
    def address_list(cls):

        
        response = cls.session.get(URL.address_url)

        print(response.content)
        print("")
        print(response.content.decode())
        print("")
        print(response.json)
        print("")

        print(cls.session.cookies)
        print("")
    
    @classmethod
    def full_text_search(cls):

        
        response = cls.session.get(URL.full_text_search_url + "福禄康瑞")

        print(response.content)
        print("")
        
        #print(response.content.decode())
        with open("zsk.html","wt") as f:
            f.write(response.content.decode())
        html_text_lines = response.content.decode().split('\r\n')

        #html_text_lines = ""
        for newline  in html_text_lines:
            if "href" in newline and "/kbs/file/show/attachment/"  in newline:
                #print(newline)
                #print( newline[newline.find("href")+6:newline.find("href")+16] )
                print( "http://10.21.0.2"+ newline[newline.find("href")+6:newline.find("target")-2 ]+"\r\n")            
        print("")
        
        #response.content.decode().filter()
        
        print(cls.session.cookies)
        print("")

if __name__ == '__main__':

    APITool.login_kbs()
    print("aaa")
    APITool.full_text_search()
