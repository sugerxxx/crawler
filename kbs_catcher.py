# -*- coding: UTF-8 -*-
'''
Created on 2019 10�� 25��

@author: surface
'''

import requests
import time
from PyQt5.QtCore import QObject
from bs4 import BeautifulSoup
from urllib import parse
import os


class URL(object):
    
    #login POST
#     loginName: qianxt0929
#     postfix: @tpl.cntaiping.com
#     password: VHAxMjM0NTY=
#      Tp123456
    login_url = "http://10.21.0.2/kbs/login"
    
    #query product GET
#     categoryId: 4ec1cea5761b3066674699
# listStyle: 1
# order: 
# sort: 
# channelId: 4ec20e1b90005754930649
# fieldId_4ec20e5963750377023276: 4ec20e5963750377023276
# fieldValue_4ec20e5963750377023276: 1099
# fieldId_4ec20e4de2876883038462: 4ec20e4de2876883038462
# fieldValue_4ec20e4de2876883038462: 
# start: 
# end: 
# _: 1571982800783
    query_product_url = "http://10.21.0.2/kbs/retrieve/ajax-list?"
    
    
    kbs_base_url = "http://10.21.0.2"
    
    #confirm_order GET
# price[]:40
# hour[]:7
# course_name[]:A�ų�
# real_time[]:7:00-8:00
# allcourse_name:A�ų�,B�ų�,C�ų�,D�ų�,
# goods_ids:298108643
# book_date:1572278400
# court_name:�Ϻ��������������ˮ���˶�ѧУ
# category_name:��ë��
# bid:22377
# cid:1
# order_type:0
# relay:0
    confirm_order_url = "https://m.quyundong.com/order/Confirm?"
    
    
    #doorder GET
#     goods_ids:298108643
# act_id:0
# code:0
# bid:22377
# cid:1
# coupon_id:0
# ticket_type:1
# utm_source:
# pay_type:
# card_no:
# relay:0
# package_type:0
# hash:017c698ec6d7fc61a449e88eeceacc0b
# _:1571888420740

    doorder_url = "https://m.quyundong.com/order/doconfirm?"

    

class APITool(QObject):
    session = requests.session()
    
    cookies_info_dict = { 
                         "SERVERID":"72b4f471436da038ecf60341309b88c2|1571985575|1571913487",
                         "PHPSESSID":"joc48cr8kopr08p2cgdqujegt3",
                         "wx_hash" : "234dc9f18382888227ec23f901864770",
                         "wx_nick_name" : "428819",
                         "wx_phone" :  "13764288196",
                         "wx_uid" : "Itnft4H4bj4Xye8bhSjI",
                         "wx_userToken":"f4%2BK5oSubzEXyeoVhyLDAIVrEA"
                         }
    
    #product_list = [1099,4041]
    product_list = [4041]
    
    product_url_dict = {}
    
    query_product_dict = {
                        "categoryId": "4ec1cea5761b3066674699",
                        "listStyle": "1",
                        "order": "",
                        "sort": "",
                        "channelId": "4ec20e1b90005754930649",
                        "fieldId_4ec20e5963750377023276": "4ec20e5963750377023276",
                        "fieldValue_4ec20e5963750377023276": "1099",
                        "fieldId_4ec20e4de2876883038462": "4ec20e4de2876883038462",
                        "fieldValue_4ec20e4de2876883038462": "",
                        "start": "",
                        "end": "",
                        "_": str(int (time.time() )*1000) 
                      }
    
    order_dict = {
                "price[]":0,
                "hour[]":0,
                "course_name[]":"",
                "real_time[]":"",
                "allcourse_name":"A�ų�,B�ų�,C�ų�,D�ų�",
                "goods_ids":0,
                "book_date":0,
                "court_name":"�Ϻ��������������ˮ���˶�ѧУ",
                "category_name":"��ë��",
                "bid":22377,
                "cid":1,
                "order_type":0,
                "relay":0

        }

    doconfirm_dict = {
                "goods_ids":"",
                "act_id":0,
                "code":0,
                "bid":22377,
                "cid":1,
                "coupon_id":0,
                "ticket_type":1,
                "utm_source":"",
                "pay_type":"",
                "card_no":"",
                "relay":0,
                "package_type":0,
                "hash":"",
                "_":0
        
        }
    
    @classmethod
    def login_kbs(cls):
        print("Step: Login...")
        data_dict = {'loginName': 'qianxt0929',
                        'postfix': '@tpl.cntaiping.com',
                        'password': 'VHAxMjM0NTY='}
        
        response = cls.session.post(URL.login_url,data_dict)

        #print(response.content)
#         print("")
        #print(response.json)
#         print("")

        print("Cookies: ", cls.session.cookies)
        print("Step complete!")
        print("")
            

    
    @classmethod
    def query_product(cls):  
        print("Step: query_product...")
        
        for product_id in APITool.product_list:
            APITool.query_product_dict["fieldValue_4ec20e5963750377023276"] = str(product_id)
        
            print("query_product_dict: " +  str(product_id) + "...")
            #for key,value in APITool.query_product_dict.items():
            #   print(key,": ",value)
            
            whole_query_product_url = URL.query_product_url + parse.urlencode( APITool.query_product_dict )
            print("query_product_url: ",whole_query_product_url)
            response = cls.session.get( whole_query_product_url )
            
            #print(response.content)
            html_text_lines = response.content.decode().split('\r\n')
            for line in html_text_lines:
                #print(line,len(line),type(line))
                if "/kbs/lore/view/" in line:
                    url = line[line.find("/kbs"):line.find(" target")-1]
                    #print(line)
                    print(url)
                    APITool.product_url_dict[str(product_id)] = url
                    
            time.sleep(0.5)
             
                    
        print("")
        for key,value in APITool.product_url_dict.items():
            print(key,": ",value)
        
        print("Step complete!")
        print("")
    
    
    
    @classmethod
    def download_product_page(cls):  
        print("Step: download_product_page...")
        
        for key,value in APITool.product_url_dict.items():
            #print(key,": ",value)
            product_id_str = str(key)
            download_url = URL.kbs_base_url + value
            print(download_url)
        
            response = cls.session.get( download_url )
            
            if not os.path.exists(product_id_str):
                os.makedirs(product_id_str)
            
            file_name = product_id_str+ "\\" + product_id_str + ".html"
            with open( file_name,"wb") as f:
                f.write(response.content)
            
            APITool.download_product_content_page(product_id_str,response.content)
            
            
            soup = BeautifulSoup(response.content,"html.parser")
            tables = soup.findAll('table')
            tab = tables[0]
            for tr in tab.findAll("tr"):
                for td in tr.findAll("td"):
                    print(td.getText())

            
            time.sleep(5)
        
        print("Step complete!")
        print("")
    
    @classmethod
    def download_product_content_page(cls,product_id_str,content):  
        html_text_lines = content.decode().split('\r\n')
        for line in html_text_lines:
            #print(line,len(line),type(line))
            if "/kbs/lore/view/content/" in line:
                url = line[line.find("/kbs"):len(line)-1]
                #print(line)
                #print(url)
                download_url = URL.kbs_base_url + url
                print(download_url)
            
                response = cls.session.get( download_url )
                
                if not os.path.exists(product_id_str):
                    os.makedirs(product_id_str)
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                script_list = soup.find_all("script")
                for item in script_list:
                    item.extract()
                
#                 third_producer = soup.find_all("script")[2]
#                 print(third_producer)
#                 
#                 third_producer_removed=third_producer.extract()  
#                 print(third_producer_removed)
#                 pause()
                soup.prettify()
                
                file_name = product_id_str+ "\\" + product_id_str + "_content.html"
                with open( file_name,'a',encoding='utf-8') as f:
                    for line in soup.contents:
                        f.write( line.find() )

    
    
    @classmethod
    def confirm_order(cls):  
        print("Step: confirm_order ")
        #whole_confirm_order_url =  APITool.add_get_info( APITool.order_dict )
        whole_confirm_order_url = URL.confirm_order_url + parse.urlencode( APITool.order_dict )
        print("whole_confirm_order_url: ", whole_confirm_order_url)
        response = cls.session.get( whole_confirm_order_url  )
        
        soup = BeautifulSoup(response.content, 'html.parser')
        input_list = soup.find_all("input")
        for item in input_list:
            #print(str(item))
            #print("")
            str_item = str(item)
            if "J_payHash" in str_item:
                soup2 = BeautifulSoup(str_item, 'html.parser')
                APITool.doconfirm_dict["hash"] = soup2.input["value"]
        

        APITool.doconfirm_dict["_"] =  str(int (time.time() )*1000) 
        
        print("doconfirm_dict:")
        for item in APITool.doconfirm_dict.items():
            print(item.key,item.value)
        print("Step complete!")
        print("")

    @classmethod
    def doorder(cls):  
        print("Step: doorder ")
        #whole_confirm_order_url =  APITool.add_get_info( APITool.order_dict )
        whole_doconfirm_dict_url = URL.doorder_url +  parse.urlencode( APITool.doconfirm_dict )
        print("doorder_url: ",whole_doconfirm_dict_url )
        response = cls.session.get(whole_doconfirm_dict_url )
        
        print(response.json())
        
        print("Step complete!")
        print("")


if __name__ == '__main__':

    APITool.login_kbs()
    APITool.query_product()
    APITool.download_product_page()

