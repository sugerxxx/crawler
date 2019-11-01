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

    login_dict = {'loginName': 'qianxt0929',
                        'postfix': '@tpl.cntaiping.com',
                        'password': "I5Qvm2wkzUPSmFr9WPBwGQ=="}
    login_url = "http://10.21.0.2/kbs/login"
    
    
    cc_main_url = "http://10.21.0.2/kbs/home/cc-main?type=home"
    
    study_url = ""
    system_url = ""
    
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
    query_product_url = "http://10.21.0.2/kbs/retrieve/ajax-list?"
    
    
    kbs_base_url = "http://10.21.0.2"
    
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
    
    
    #product_list = [4041]
    #product_list = [1099,4041]

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

    product_url_dict = {}
    
    base_path = "kbs\\"
  
    
    @classmethod
    def login_kbs(cls):
        print("Step: Login...")

        response = cls.session.post(URL.login_url,URL.login_dict)
        
        print("Cookies: ", cls.session.cookies)

        response = cls.session.get(URL.cc_main_url)
        
        soup = BeautifulSoup(response.content,"lxml")
        iframe_list = soup.find_all("iframe")
        URL.study_url = URL.kbs_base_url + iframe_list[0]["src"]
        URL.system_url =URL.kbs_base_url +  iframe_list[1]["src"]
        
        print("study_url", URL.study_url)
        response = cls.session.get(URL.study_url)
        #print(response.content.decode())
        soup_study = BeautifulSoup(response.content,"lxml")
        print(str(soup_study.body.string).strip())

        print("system_url", URL.system_url )
        response = cls.session.get( URL.system_url )
        #print(response.content.decode())
        soup_system = BeautifulSoup(response.content,"lxml")
        print(str(soup_system.body.string).strip())

        print("Cookies: ", cls.session.cookies)
        
        print("Logging Step complete!")
        print("")
        

    
    @classmethod
    def query_product(cls):  
        print("Step: query_product...")
        
        
        for product_id in APITool.product_list:
            URL.query_product_dict["fieldValue_4ec20e5963750377023276"] = str(product_id)
        
            print("Product: " +  str(product_id) + "begins...")
            #for key,value in APITool.query_product_dict.items():
            #   print(key,": ",value)
            
            whole_query_product_url = URL.query_product_url + parse.urlencode( URL.query_product_dict )
            print("query_product_url: ",whole_query_product_url)
            response = cls.session.get( whole_query_product_url )
            
            #print(response.content)
            #print(ParseTool.find_url_from_response(response.content,"/kbs/lore/view/"))
            #print(ParseTool.find_url_from_response2(response.content,"/kbs/lore/view/"))
            '''
            html_text_lines = response.content.decode().split('\r\n')
            for line in html_text_lines:
                #print(line,len(line),type(line))
                if "/kbs/lore/view/" in line:
                    url = line[line.find("/kbs"):line.find(" target")-1]
                    #print(line)
                    print(url)
             '''       
            product_url = ParseTool.find_url_from_response(response.content,"/kbs/lore/view/")
            if product_url != "":
                APITool.product_url_dict[str(product_id)] = ParseTool.find_url_from_response2(response.content,"/kbs/lore/view/")
                    
            time.sleep(random.random())

        for key,value in APITool.product_url_dict.items():
            print(key,": ",value)
        
        print("Product Querying Step complete!")
        print("")
    
    
    
    @classmethod
    def download_product_page(cls):  
        print("Step: download_product_page...")
        
        i = 1
        for key,value in APITool.product_url_dict.items():
            print(key,": ",value)
            product_id_str = str(key)
            download_url = URL.kbs_base_url + value
            print("download_url",download_url)
        
            
            
            if  os.path.exists(APITool.base_path + product_id_str):
                shutil.rmtree(APITool.base_path + product_id_str)
            os.makedirs(APITool.base_path + product_id_str)
            
            response = cls.session.get( download_url )
            soup = BeautifulSoup(response.content,"html.parser")
            
            
            #去除正文
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
                #print(file_name)
                for link in item.find_all("a"):
                    #print(link["href"])
                    if "/kbs/upload/down-cdn" in link["href"] :
                        link_href = link["href"]
                        whole_file_name = APITool.base_path +product_id_str + "/" + file_name
                        ParseTool.downloading_file(cls.session,URL.kbs_base_url + link_href,whole_file_name)
                        

            div_content = APITool.download_product_content_page(APITool.base_path +product_id_str,response.content)
            #print("div_content",div_content)
            #print("")
            soup.find(id="zw").append(div_content)
            
            file_name = APITool.base_path +product_id_str+ "\\" + product_id_str + ".html"
            ParseTool.save_soup(soup,file_name)
#             
#             tables = soup.findAll('table')
#             tab = tables[0]
#             for tr in tab.findAll("tr"):
#                 for td in tr.findAll("td"):
#                     print(td.getText())

            
            if i < len(APITool.product_list):
                i = i + 1
                sleeptime=20+int(random.random()*20)
                print("sleeptime:" ,sleeptime)
                time.sleep(sleeptime)
                
            print("")
            
        print("Downloading Product Step complete!")
        print("")
    
    @classmethod
    def download_product_content_page(cls,path,content):  
        html_text_lines = content.decode().split('\r\n')
        for line in html_text_lines:
            #print(line,len(line),type(line))
            if "/kbs/lore/view/content/" in line:
                url = line[line.find("/kbs"):len(line)-1]
                #print(line)
                #print(url)
                product_content_url = URL.kbs_base_url + url
                print("product_content_url",product_content_url)
            
                response = cls.session.get( product_content_url )
                
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                img_list = soup.find_all("img")
                for img in img_list:

                    picture_name =  str(img["src"])[str(img["src"]).rfind("/")+1:len(str(img["src"]))]
                    #print(picture_name)

                    ParseTool.downloading_file(cls.session,URL.kbs_base_url + img["src"] ,path + "/" + picture_name)

                    img["src"] = picture_name

                script_list = soup.find_all("script")
                for item in script_list:
                    item.extract()

                
                div_content = soup.find(id = "content")
            
                return div_content

if __name__ == '__main__':

    APITool.login_kbs()
    APITool.query_product()
    APITool.download_product_page()

