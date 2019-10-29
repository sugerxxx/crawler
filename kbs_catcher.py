# -*- coding: UTF-8 -*-
'''
Created on 2019 10�� 25��

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


class URL(object):
    
    #login POST
#     loginName: qianxt0929
#     postfix: @tpl.cntaiping.com
#     password: VHAxMjM0NTY=
#      Tp123456
    login_url = "http://10.21.0.2/kbs/login"
    
    
    
    prelogin_url = "http://10.21.0.2/study/sso/preLogin?loginName=qianxt0929@tpl.cntaiping.com&SESSION_ID=##SESSION_ID##!##########&SESSION_LOGIN_MODE=LOGIN_MODE_LOCAL&t="
    
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
    

    

class APITool(QObject):
    session = requests.session()
    
    cookies_info_dict = { 
                        "AlteonP":"AFKfEAIAFQoAlhMpAAwSRg$$",
                        "kmpro_tp_v5":"L54QT_OXu-LGTv2d9p6fRWsiy43BSJkqo2E8F9KIERcPu6MwFZpE!1293138469"#,
                        #"JSESSIONID":"9pURVcGFwRGyE2SBtrlSd6id1aA2DwdMG5Auf9DuZV2RbQOYh-xr!1293138469"
        
                         }
    
    product_list = [4041]
    #product_list = [1099,4041]
    '''
    product_list = [1018,
1099,
1100,
1101,
1148,
1161,
1177,
1180,
1181,
1185,
1201,
1202,
1203,
1204,
1205,
1223,
1224,
1225,
1235,
1236,
1241,
1242,
1243,
1244,
1245,
1248,
1252,
1253,
1254,
1256,
1257,
1259,
1263,
1265,
1266,
1267,
1268,
4005,
4006,
4007,
4008,
4009,
4010,
4011,
4012,
4017,
4021,
4023,
4028,
4031,
4032,
4033,
4034,
4035,
4036,
4037,
4038,
4039,
4041,
4042,
4045,
4046,
4048,
4049,
4050,
4051,
4055,
4056,
4057,
4058,
4059,
4060,
4061,
4062,
4063,
4065,
4066,
4067,
4068,
4074]
    '''
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
    
   
    
    @classmethod
    def login_kbs(cls):
        print("Step: Login...")
        
        data_dict = {'loginName': 'qianxt0929',
                        'postfix': '@tpl.cntaiping.com',
                        'password': "I5Qvm2wkzUPSmFr9WPBwGQ=="  }
        
        #print("Cookies: ", cls.session.cookies)

        
        '''
        headers = {
            "Host": "10.21.0.2",
            "Origin": "http://10.21.0.2",
            "Referer": "http://10.21.0.2/kbs/login",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
            }
         '''
        
        #response = cls.session.post(URL.login_url,data_dict,headers=headers)
        response = cls.session.post(URL.login_url,data_dict)
        
        '''
        print("Cookies: ", cls.session.cookies)
        print("kmpro_tp_v5: ", cls.session.cookies.get("kmpro_tp_v5"))
        kmpro_tp_v5_url = "http://10.21.0.2/kbs/;kmpro_tp_v5=" + cls.session.cookies.get("kmpro_tp_v5")
        print("kmpro_tp_v5_url",kmpro_tp_v5_url)
        response = cls.session.get(kmpro_tp_v5_url)
        '''

        
        #for key,value in APITool.cookies_info_dict.items():
        #   cls.session.cookies.set(key, value, domain="10.21.0.2")
        print("Cookies: ", cls.session.cookies)
        print("")
        
        
        response = cls.session.get("http://10.21.0.2/kbs/home")
        #print(response.content)
        
        response = cls.session.get("http://10.21.0.2/kbs/home/cc")
        #print(response.content)
        response = cls.session.get("http://10.21.0.2/kbs/home/cc-main?type=home")
        
        soup = BeautifulSoup(response.content,"html.parser")
        iframe_list = soup.find_all("iframe")
        study_url = iframe_list[0]["src"]
        system_url = iframe_list[1]["src"]
        
        
            
        #print(response.content.decode())
        
        
        
#         headers={
#                             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
#                             "Accept-Encoding": "gzip, deflate",
#                             "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#                             "Connection": "keep-alive",
#                             #"Cookie":APITool.cookies_info_dict,
#                             "Host": "10.21.0.2",
#                             "Referer":"http://10.21.0.2/kbs/home/cc-main?type=home",
#                             "Upgrade-Insecure-Requests": "1",
#                             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
#                         }
        
        #URL.prelogin_url = URL.prelogin_url.replace("##SESSION_ID##",  str(cls.session.cookies.get("SESSION_ID")) )
        
        
        #URL.prelogin_url = URL.prelogin_url.replace("##########",  str(int(time.time()) *1000) )
        #print("prelogin_url", URL.prelogin_url)
        print("study_url", URL.kbs_base_url + study_url)
        response = cls.session.get(URL.kbs_base_url + study_url )
        print(response.content.decode())
        
        print("system_url", URL.kbs_base_url + system_url)
        response = cls.session.get(URL.kbs_base_url + system_url)
        print(response.content.decode())
        
        
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
                    
            #time.sleep(0.5)
             
                    
        print("")
        for key,value in APITool.product_url_dict.items():
            print(key,": ",value)
        
        print("Step complete!")
        print("")
    
    
    
    @classmethod
    def download_product_page(cls):  
        print("Step: download_product_page...")
        
        for key,value in APITool.product_url_dict.items():
            print(key,": ",value)
            product_id_str = str(key)
            download_url = URL.kbs_base_url + value
            print(download_url)
        
            response = cls.session.get( download_url )
            
            if  os.path.exists(product_id_str):
                shutil.rmtree(product_id_str)
            os.makedirs(product_id_str)
            
            soup = BeautifulSoup(response.content,"html.parser")
            
            iframe_list = soup.find_all("iframe")
            for item in iframe_list:
                item.extract()
            #soup.prettify()
            
            for remove_div_id in ["tagModal","favoriteModal","userModal","correctionModal","replyContent","nearLoreList"]:
                remove_div_list = soup.find_all( id = remove_div_id)
                for item in remove_div_list:
                    item.extract()
            
            script_list = soup.find_all("script")
            for item in script_list:
                item.extract()
            
            fujian_div = soup.find(id="fujian")
            li_list = fujian_div.find_all("li")
            for item in li_list:
                for string_text in item.stripped_strings:
                    file_name = repr(string_text).strip("'")
                    break
                #file_name = "太平真爱定期寿险2018产品培训课件.pdf"
                print(file_name)
                for link in item.find_all("a"):
                    #print(link["href"])
                    if "/kbs/upload/down-cdn" in link["href"] :
                        link_href = link["href"]
                        #link_href = link_href.replace("down-cdn","down-local")
                        #link_href = link_href[0:link_href.rfind("/")]
                        
#                         headers={
#                             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
#                             "Accept-Encoding": "gzip, deflate",
#                             "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#                             "Connection": "keep-alive",
#                             "Host": "10.21.0.2",
#                             "Referer":download_url,
#                             "Upgrade-Insecure-Requests": "1",
#                             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
#                         }
#                         for key,value in headers.items():
#                             print( key,value)
                        #print(headers)
                        
                        print("downloading..." , URL.kbs_base_url + link_href ,product_id_str + "/" + file_name)
                        

                        
                        #response= cls.session.get("http://10.21.0.2/kbs/upload/down-cdn/78eb2bba-71f2-4194-b71e-bf3b2cf6a284/0?dn=0")
                        file_response = cls.session.get(URL.kbs_base_url + link_href )
                        #print(file_response.headers)
                        #print(response.content)
                        f = open(product_id_str + "/" + file_name, "wb")
                        f.write(file_response.content)
                        f.close()
                        



            
            div_content = APITool.download_product_content_page(product_id_str,response.content)
            #print("div_content",div_content)
            print("")
            
            soup.find(id="zw").append(div_content)
            
            

                         
                
            file_name = product_id_str+ "\\" + product_id_str + ".html"
#             with open( file_name,"wb") as f:
#                 f.write(response.content)
            
            content_file = open(file_name,'a',encoding='utf-8')
            print(soup.prettify(), file = content_file)
            content_file.close() 
            

#             
#             tables = soup.findAll('table')
#             tab = tables[0]
#             for tr in tab.findAll("tr"):
#                 for td in tr.findAll("td"):
#                     print(td.getText())

            
            
            sleeptime=20+int(random.random()*20)
            print("sleeptime:" ,sleeptime)
            time.sleep(sleeptime)
        
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
                
                #if not os.path.exists(product_id_str):
                #   os.makedirs(product_id_str)
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                img_list = soup.find_all("img")
                for img in img_list:
                    #print(img)
                    print("downloading...",URL.kbs_base_url + img["src"])
                    #print(str(img["src"]).rfind("/"),len(str(img["src"]))-1)
                    picture_name =  str(img["src"])[str(img["src"]).rfind("/")+1:len(str(img["src"]))]
                    print(picture_name)
                    #request.urlretrieve(URL.kbs_base_url + img["src"],  product_id_str + "/" + picture_name)
                    
                    file_response = cls.session.get(URL.kbs_base_url + img["src"])
                        #print(file_response.headers)
                        #print(response.content)
                    f = open(product_id_str + "/" + picture_name, "wb")
                    f.write(file_response.content)
                    f.close()
                    
                    img["src"] = picture_name
                    #print(img)
                    #print(img["src"])
                
                script_list = soup.find_all("script")
                for item in script_list:
                    item.extract()
                

                
#                 file_name = product_id_str+ "\\" + product_id_str + "_content.html"
#                 content_file = open(file_name,'a',encoding='utf-8')
#                 print(soup.prettify(), file = content_file)
#                 content_file.close() 

                div_content = soup.find(id = "content")
                return div_content

if __name__ == '__main__':

    APITool.login_kbs()
    APITool.query_product()
    APITool.download_product_page()

