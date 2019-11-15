# -*- coding: UTF-8 -*-

'''
Created on 2019��11��14��

@author: hucy1129
'''




import requests
import time
from PyQt5.QtCore import QObject
from bs4 import BeautifulSoup
from urllib import parse,request
import shutil
import os
import random
import json

class Order_Param(object):
    itemId = 607400046123
    price = 298
    skuId = 0
    

class URL(object):
    
    query_product_dict = {
        "id" :  Order_Param.itemId
                    }

    query_product_url = "https://detail.damai.cn/item.htm?"
    
    
    order_confirm_dict = {
        "exParams":  '{"damai":"1","channel":"damai_app","umpChannel":"10002","atomSplit":"1","serviceVersion":"1.8.5","umidToken":"T4C89284610DAA1B8624C569157E320AA34185717675E849819C9FE1263","ua":"121#EDwlk+DD8TllVlyV+BH+l1ZU3aXWx3jVlGu2k2b2OwwJWG1u57eTPMLYAcfdxujVlGuY+zPIDM9lA3FnEGDIVlHH8VEMKujlswgY+z/ILMlVA3rnEkDIll9YOc8fxujVlGuY+zpIDM9lOQrn75DIlwV7EuDYFQQVwkbvsb5SMtFPD0rgXSBbbZ3glWfopCibCP7T83Smbgi0CeHaF960C6sDnjx9pl9lMaxUM3BmC6JbCeHaQ9ibbZsbnjxSpXb0C6048uSmbgi0CeHXF960C6ibn6ZSWNYyU5+g8uBmbMUgs+JEQzRRxZ5dJOA+pwSbCZ0T7lyVSrDbt5calfRK+Lroz84rXpXK5bC7eieT/bk7wlL1pjFEP5eA5saCd/Xeey54pnR50kpH/j0PKDKHITlHjQRt2uqOvGWVfKhwrPHKj5tFPCSI9rZfNk7xWn4GAypPW2Y6SDFttkoJ8S/LnC/iylgBT+mUFm4cj0Y23jDy3l/s8ozOvByO3u1wxf7Zt9e0g4mcUjIuSInrwwV++DOtMCOGAvp+FcviRFMhmspBjE6Awbc86UFNjq32aQbxTMdL6Zs6GXG9EOIFmVyD2aZ9Wa5taXnQijUqpYD4A97VhlpX9WZyP2exgnXdE1xbR1glfua1S2LkXfyEEvyhOUnVyPtRA1Ysu2nmKpPHfLLffuI5T/heGNolOTjX"}',
        #"exParams":  '{"damai":"1","channel":"damai_app","umpChannel":"10002","atomSplit":"1","serviceVersion":"1.8.5"}',
        "buyParam": str(Order_Param.itemId) + "_1_" + str(Order_Param.skuId) ,       #item_id,   skuid   607400046123_1_4262519829912
        "buyNow": "true",
        "spm": "a2oeg.project.projectinfo.dbuy"
                     }
    
    order_confirm_url = "https://buy.damai.cn/orderConfirm?"
    
    
    get_umjson_dict = {
        "data": "106!MUqmc0clzdnH+NixHmHI4lxmYX+lQzGzUUam0LHtKjRU56cm9rQby+bZ0PHCncyIKV4odp7HxfbvZ28EKYD9SajrmnXmkmNZlYu2E2nUH/7cDZUDbgGZ6752xZCB3P0GOcFM5rLosAHgFOB+bBLKcQ8Mwn5w790rxiSkMfdEOCh1URFsw78OGUBmnv7SP7EgXqE72E7w56UzU2G/um6XOCuczYCpPZEL1DaU6u3P/DumRB3rETvQ46gW16IHSdYU42kU6IcPsRaUxzEG/b2/hKH68klfkKu/6e95DBa3Q9EoJe/joDBHvId8LmGwiqr32msKPDDYYgoZcjt4MA7XbFWe4NoKXdKC6MN/cMuB4wPXzztFdhaPjp4NhNfZ0bMPoVejEQhDp/0oR8Vxd8wNBswF5mXOEe/oucdl0InOBB9YUUVEmlibaupTON7316xNTOm3kB9KQnY8NujBQJcK5i1Hq5W2OpcT3rMXeVVXdlCb9xrvn4jh2Mi96EtOdNMu7NAfIX7a4CzDFTf+111n7E+PQB/IElHCjC7EHG4k+aQE3N7+4NUc7r4zuSt1neCeHz8DIIpWXmxvLUYqjGbN3+SCfbEXxzL76Ab4eJyefPrRn9ngyYNbZ5X6uPJtVcALFULE8MhweCHzlH7S4SZAKI6o0ToPAL8R70TvzXonXgfF+XmKXrzjtNU8P847TWUvuDAs8HQcsDcLWZAN",
        "xa": "mec-tradeportal",
        "xt": ""
        }
    
    get_umjson_url = "https://ynuf.aliapp.org/service/um.json"
    
    
class ParseTool(object):
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
    
    
    cookies_info_dict = { 
                         "damai.cn_nickName":  "%E9%BA%A6%E5%AD%9008XYa",   
                         "damai.cn_user":"LTx9ZvxbEnYayeoeNhQlyo36Ku1zmbpM7+/edpTTPbhCuNq+b9wwkK0YcAX4CQNnGxb2+Rjuqig=",
                         "damai.cn_user_new" : "LTx9ZvxbEnYayeoeNhQlyo36Ku1zmbpM7%2B%2FedpTTPbhCuNq%2Bb9wwkK0YcAX4CQNnGxb2%2BRjuqig%3D",
                         "h5token" : "5fb2ff9462fb4c29973504969ca2a88f_1_1",
                         "damai_cn_user" :  "LTx9ZvxbEnYayeoeNhQlyo36Ku1zmbpM7%2B%2FedpTTPbhCuNq%2Bb9wwkK0YcAX4CQNnGxb2%2BRjuqig%3D",
                         "loginkey" : "5fb2ff9462fb4c29973504969ca2a88f_1_1",
                         "user_id":"119457281",
                         "cna": "KI09FYECMyYCATr2i7b62V1e",
                         "cookie2": "12430ddbfebd69d4430e92e4aca7530d",
                         "t": "f4e9beb3eb9c1d29d99559cb0cb366ee",
                         "_tb_token_": "e71b70663817a",
                         "_hvn_login": "18",
                         "_m_h5_tk": "69682e14cc8a2805fbd38cb372b4a26f_1573721967083",
                         "_m_h5_tk_enc": "fbb0d8a5940a25dcdb65f1cb8a81718b",
                         "munb": "4294602849",
                         "csg": "6baa5c4b",
                         "l": "dBQhfqvgqlmFWE6SXOCanurza77OSIRYmuPzaNbMi_5BH6L_Ua7OkBWLcFp6VjWfMH8B41jxjkw9-etki7h8Swq7dDZabxDc.",
                         "isg": "BHV1I4dhRPoxu6Ay214QosXLhPEllqgrBY0FEveaM-w7zpXAv0aE1atMGNLdikG8",
                         "c_csrf" : "f9fbbc1b-cb5c-4f79-bff4-c126c824659a"
                         }
    buy_cookies_info_dict = {
                        "c_csrf" : "f9fbbc1b-cb5c-4f79-bff4-c126c824659a"
                        }
    
    @classmethod
    def login_damai(cls):
        print("Step: Login...")
        
        for key,value in APITool.cookies_info_dict.items():
            cls.session.cookies.set(key, value, domain=".damai.cn")
        print("cookies: ",cls.session.cookies)

        print("Logging Step complete!")
        print("")
        

    
    @classmethod
    def query_product(cls):  
        print("Step: query_product...")
        
        whole_query_product_url = URL.query_product_url + parse.urlencode( URL.query_product_dict )
        print(whole_query_product_url)
        
        response = cls.session.get(whole_query_product_url)
        soup = BeautifulSoup(response.content,"lxml")
        
        dataDefault = soup.find( id="dataDefault")
        #print(dataDefault)
        #print(dataDefault.string)
        dataDefault_dict = json.loads(dataDefault.string)
        #dataDefault_dict = dataDefault.value
        #print(dataDefault_dict)
        skuList = dataDefault_dict["performBases"][0]["performs"][0]["skuList"]
        print(skuList)
        for sku_dict in skuList:
            #print(sku_dict)
            if sku_dict["price"] == Order_Param.price:
                Order_Param.skuId = sku_dict["skuId"]
        print(Order_Param.skuId)
        
        print("Product Querying Step complete!")
        print("")
    
    
    @classmethod
    def get_umjson(cls):
        print("Step: get_umjson_page...")
        
        response = cls.session.post(URL.get_umjson_url,URL.get_umjson_dict)
        print(response.content)
        
        umidToken = response.json()
        print(umidToken["tn"])
        URL.order_confirm_dict["exParams"]["umidToken"] = umidToken["tn"]
        print("Get Umjson complete!")
        print("")
        
    
    @classmethod
    def order_confirm_page(cls):  
        print("Step: order_confirm_page...")
        
        whole_order_confirm_url = URL.order_confirm_url + parse.urlencode( URL.order_confirm_dict )
        print(whole_order_confirm_url)
        
        
        header = {"referer": "https://detail.damai.cn/item.htm?id=607400046123"}
        response = cls.session.get(whole_order_confirm_url,headers=header)
        print(response.content)
        
        
            
        print("Order Confirm complete!")
        print("")
    

        

if __name__ == '__main__':
    
    time1 = time.time()
    
    APITool.login_damai()
    APITool.query_product()
    APITool.get_umjson()
    APITool.order_confirm_page()
    
    time2 = time.time()
    print("Spent:",time2-time1," sec.")

