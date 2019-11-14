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


class URL(object):
    
    query_product_dict = {
        "id" :  607400046123
                    }
    
    query_product_url = "https://detail.damai.cn/item.htm?"
    
    
    
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
                         "damai.cn_user":"Il6sNUquqJ8oVi6R5mKPUGpXmBV0UrD4Z5+BBMMdk5BCuNq+b9wwkK0YcAX4CQNnGxb2+Rjuqig=",
                         "damai.cn_user_new" : "Il6sNUquqJ8oVi6R5mKPUGpXmBV0UrD4Z5%2BBBMMdk5BCuNq%2Bb9wwkK0YcAX4CQNnGxb2%2BRjuqig%3D",
                         "h5token" : "5fb2ff9462fb4c29973504969ca2a88f_1_1",
                         "damai_cn_user" :  "Il6sNUquqJ8oVi6R5mKPUGpXmBV0UrD4Z5%2BBBMMdk5BCuNq%2Bb9wwkK0YcAX4CQNnGxb2%2BRjuqig%3D",
                         "loginkey" : "5fb2ff9462fb4c29973504969ca2a88f_1_1",
                         "user_id":"119457281"
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
        print(dataDefault)
        print(dataDefault.string)
        
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
            
            
            #ȥ������
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
                #file_name = "̫ƽ�氮��������2018��Ʒ��ѵ�μ�.pdf"
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

    APITool.login_damai()
    APITool.query_product()


