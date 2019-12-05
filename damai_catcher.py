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
from fake_useragent import UserAgent
import hashlib
#import execjs
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import NoEncryption,Encoding, PrivateFormat, PublicFormat
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization  

#from crypto import PublicKey
#from crypto.PublicKey import RSA
#from crypto import Random



class Order_Param(object):
    #ua = UserAgent(use_cache_server=False)
    #ua_chrome=ua.chrome
    ua_chrome = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"  #seems related with ua
    itemId = 607400046123
    price = 298
    skuId = 0
    csrf_token = ""
    hsiz = ""
    umidToken = ""
    umidEncryptAppName = ""
    #window_token = ""
    umjson_tn_tn = ""
    umjson_tn_id = ""
    

class URL(object):
    
    passport_url = "https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F"
    
    ipassport_url = "https://ipassport.damai.cn/mini_login.htm?"
    
    ipassport_dict = {
            "lang": "zh_cn",
            "appName": "damai",
            "appEntrance": "default",
            "styleType": "vertical",
            "bizParams": "",
            "notLoadSsoView": "true",
            "notKeepLogin": "false",
            "isMobile": "false",
            "showSnsLogin": "false",
            "regUrl": "//passport.damai.cn/register",
            "plainReturnUrl":"//passport.damai.cn/login",
            "returnUrl": "https://passport.damai.cn/dologin.htm?redirectUrl=https%253A%252F%252Fwww.damai.cn%252F&platform=106002",
            "rnd": random.random() }
    
    eg_js_url = "https://log.mmstat.com/eg.js"
    
    check_url = "https://ipassport.damai.cn/newlogin/account/check.do?appName=damai&fromSite=-2"
    
    check_dict = {
                "oginId": "13764288196",
                "ua": "121#pSmlkthHVqllVl2OG8Hel1ZU3aXWxOwYlGr6qsG21l5EKPFupUI7VmwmCaFdK5jVllKY+zPIDMlSAQQcVFT3ll9YAcWZKujVVy5H4FJ5KM9lOlrJEGiIlMLYAcfdK5jVlmuY+zpIxM9VO3rnEkDIll9YOc8dKkjVlwr7jPXUqMoVG0bvsbc9M98ze0bWkBu9CbibYQhEU960C6Jbnj2SRCD0CZe483VhlRjGprzXF9WbMXF3nnxVpb6FlwRT8uzDCbi0CN+SFtFbbZsbnjxSpXb0C60Z8uBmbZs0CeHXF960C60lnFOmcyYaG3an8up0MsUoFNMGKynVdf+wJoLVTMSbkX7T83pWVwmG58VRDqjTtId3R68hM5dj4U/bQztr7fMDfYTGYGgGr4BBiAYNEXQhGET0EwS77S3GFc55gmSpUBCfM2mNHiN9DFe6Yr+KhMujD+V8W4XJfyQ3rNxPJWLmsO11RCJvrOaTAzUOr+Dt0FJrjDLio48zzdixHJ/b9Edf6jTXP0EcmIDXBiFlRhMvBsfnVNCMOq13LjFI5ZB+nryc5/8a0QnB8N/QUGK2DCEoP9SUp3O3pkmDjDxQn2NQNhUUuKNwjakORynDO4ruAaiNkhSMR7jO5NkM/TxwFsol5TMhpENFe50A16GlRJoU2nwzE2AVxHYFno//d6P7CDjCqTpRnq0ae35hPOkxbxRBrMGIQlijs8fB746e7EpYRDL4Kov04P9EqtjRhCeAKKuqecAPL8nls8eErhBZTYcb2mGs6Nv/9ebKJqAfw7tMB+Y0DObfa31jt/cbj9RD2WmsnYEqfNxkPPJyMcVe1WjkF/rEfsKMWuiYO5U9N4ixBWF3CXFU/aDFLU0jl1SD6M3vplQnyRaaUY6auualPwKls6tHIP641p/2CZF5Vk9GrkpaDsVNDQoA4v9jLNaU/f2PhvRdwxSd33prAJ2Onl/6a/ly1GIz4MncmR0FQfIKWWg6XixIPykPiFbRaZ1zUwXXeqcQbNHqf5lnc9khJVd6zoKBwEU6KZPX5n1XgjppUeTgH6C9mbxUleQSVjqjnrwRrLQlXr+rfy9x4B/EadxUXu+L5LIgeKcaeoOy0UbIgDPFSqzZ+2P/Txciwa5seI4HpyVZ7RYLtx5C6PqKfn78aLii8Y2mEnYFZpHKJ1ELinqul7M8kCbuwsbNjF9lbOJ/MTYdZcKIVVbqSoYqfQiJpBR0uImFA6fcW4iN340TnZw3lj5G+4TqdGgYZvoaAjwSdvqw8cgGq3O/mPKu/aVshhvP+TbjKHo5b8v7S5D/n5fCewU/K53Ld8E8WKxi93Ihcu1FA6v0AFrocmiZYnwKg0SJMN32tXgUgsm=",
                "umidGetStatusVal": "255",
                "screenPixel": "1680x1050",
                "navlanguage": "zh-CN",
                #"navUserAgent": Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
                "navUserAgent": Order_Param.ua_chrome,
                "navPlatform": "Win32",
                "appEntrance": "damai",
                "appName": "damai",
                "bizParams": "",
                "csrf_token": Order_Param.csrf_token,
                "fromSite": "-2",
                "hsiz": Order_Param.hsiz,
                "isMobile": "false",
                "lang": "zh_CN",
                "mobile": "false",
                "returnUrl": "https://passport.damai.cn/dologin.htm?redirectUrl=https%253A%252F%252Fwww.damai.cn%252F&platform=106002",
                "umidToken": Order_Param.umidToken
        }
    
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
        "xa": "havana-damai",
        "xt": Order_Param.umidToken
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
    
    cookies_info_dict2 = { 
                         "l": "dBQhfqvgqlmFWE6SXOCanurza77OSIRYmuPzaNbMi_5BH6L_Ua7OkBWLcFp6VjWfMH8B41jxjkw9-etki7h8Swq7dDZabxDc.",
                         "isg": "BHV1I4dhRPoxu6Ay214QosXLhPEllqgrBY0FEveaM-w7zpXAv0aE1atMGNLdikG8",
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
    def login2_damai(cls):
        

        
        print("Step: Login...")
        
        #user_agent = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
        user_agent = {"User-agent":Order_Param.ua_chrome}
        #print(user_agent)
        
        for key,value in APITool.cookies_info_dict2.items():
            cls.session.cookies.set(key, value, domain=".damai.cn")
        response = cls.session.get(URL.passport_url,headers = user_agent)    
        whole_ipassport_url = URL.ipassport_url + parse.urlencode( URL.ipassport_dict )
        print(whole_ipassport_url)
        response = cls.session.get(whole_ipassport_url)     
         
        soup = BeautifulSoup(response.content,"lxml")
        script_list = soup.find_all( "script")
        
        #print(str(script_list[1].string))
        window_list = str(script_list[1].string).split("\n")
        for window in window_list:
            if "window.viewData" in window:
                #print(window)
                viewData_dict = json.loads(window[window.find("{"):len(window)-1])
                Order_Param.csrf_token = viewData_dict["loginFormData"]["csrf_token"]
                Order_Param.hsiz =  viewData_dict["loginFormData"]["hsiz"]
                Order_Param.umidToken = viewData_dict["umidToken"]
                Order_Param.umidEncryptAppName = viewData_dict["umidEncryptAppName"]
                #print(Order_Param.umidToken)
  
        #print(str(script_list[3].string))
        '''
        window_list = str(script_list[3].string).split("\n")        
        for window in window_list:
            if "token" in window:
                #print(window)
                Order_Param.window_token = window[window.find('"')+1:len(window)-2]
                print(Order_Param.window_token)
         '''       
        response = cls.session.get(URL.eg_js_url)
        cna_string = response.content.decode()
        #print(cna_string)
        cna = cna_string[cna_string.find("goldlog.Etag")+14:cna_string.find(";goldlog.stag")-1]
        print(cna)
        cls.session.cookies.set("cna", cna, domain=".damai.cn")
        
        print("cookies: ",cls.session.cookies)

        print("Logging Step complete!")
        print("")

    @classmethod
    def check_name(cls):
        print("Step: check_name...")        
        
        head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 'Connection': 'close'}

        
        response = requests.post(URL.check_url,data=URL.check_dict,headers=head)
        
        print(response.json())
        
        print("cookies: ",cls.session.cookies)

        print("check_name Step complete!")
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
        
        umjson_tn = response.json()
        #print(umjson_tn["tn"])
        Order_Param.umjson_tn_tn = umjson_tn["tn"]
        Order_Param.umjson_tn_id = umjson_tn["id"]
        print(Order_Param.umjson_tn_tn)
        print(Order_Param.umjson_tn_id )
        
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
    password = b"Um111111"
    #rsaExponent = "010001"
    rsaExponent = '010001'
    #rsaExponent = 65537
    rsaModulus = 'd3bcef1f00424f3261c89323fa8cdfa12bbac400d9fe8bb627e8d27a44bd5d59dce559135d678a8143beb5b8d7056c4e1f89c4e1f152470625b7b41944a97f02da6f605a49a93ec6eb9cbaf2e7ac2b26a354ce69eb265953d2c29e395d6d8c1cdb688978551aa0f7521f290035fad381178da0bea8f9e6adce39020f513133fb'
    
    
    
    def rsa_encrypt(message,rsaExponent, rsaModulus):
        '''
        根据cryptography包下的rsa模块，对指数模数进行处理生成公钥
        :param rsaExponent:指数
        :param rsaModulus:模数
        :return:公钥
        '''
        rsaExponent = int(rsaExponent, 16)  # 十六进制转十进制
        rsaModulus = int(rsaModulus, 16)
    
        pubkey = rsa.RSAPublicNumbers(rsaExponent, rsaModulus).public_key(default_backend())
        
        pem = pubkey.public_bytes(  encoding=serialization.Encoding.PEM,  format=serialization.PublicFormat.SubjectPublicKeyInfo   )  
  
        
        
        print("pub:",pubkey)
        print("pem:",pem)

        
        #message = b"encrypted data"
        print(message)
    
        ciphertext = pubkey.encrypt(
            message,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                        algorithm=hashes.SHA256(),
                                        label=None ) 
            )
        
        print(ciphertext)

        

        
        return ciphertext
    
    ciphertext = rsa_encrypt(password,rsaExponent, rsaModulus)
    input()

    APITool.login2_damai()
    APITool.get_umjson()
    APITool.check_name()
    #APITool.query_product()
    #APITool.order_confirm_page()
    
    time2 = time.time()
    print("Spent:",time2-time1," sec.")

