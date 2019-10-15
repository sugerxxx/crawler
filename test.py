# -*- coding: UTF-8 -*-
'''
Created on 2019 10 9日

@author: surface
'''

#from PyQt5.Qt import  *
import requests
from PyQt5.QtCore import QObject

class URL(object):
    
    #yzm POST
#     loginName: qianxt0929
#     postfix: @tpl.cntaiping.com
#     password: VHAxMjM0NTY=
#      Tp123456
    yzm_url = "https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand"
    
    #init POST
    init_url = "https://kyfw.12306.cn/otn/index/initMy12306Api"
    
    #queryMyOrder
    query_myorder_url = "https://kyfw.12306.cn/otn/queryOrder/queryMyOrder"
    
    #query_ticket GET
    
    query_ticket_url = "https://kyfw.12306.cn/otn/leftTicket/query?"
    #https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-10-16&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=BJP&purpose_codes=ADULT
    
    #init_dc POST
    init_dc_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    #order_ticket  POST
#     _json_att: 
#     REPEAT_SUBMIT_TOKEN: 03e018fecc5f505b0a49aa0a6fccfb82
    order_ticket_url = "https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"
    

class APITool(QObject):
    session = requests.session()
    globalRepeatSubmitToken = ""
    @classmethod
    def download_yzm(cls):
        print("download_yzm")
        response = cls.session.get(URL.yzm_url)
#         with open("yzm.jpg","wb") as f:
#             f.write(response.content)
#         print(response.content)
#         print("")
#         print(response.json)
#         print("")

        #print(cls.session.cookies)
        tk = "jGx43w7Yi1YZfVHCA496HkZBhrm96p275V6CbqQookIsdp1p0"
        cls.session.cookies.set("tk", tk, domain="kyfw.12306.cn")
        #cls.session.cookies.set("JSESSIONID", "F92C175A6CA7FD502756FAF42717883E")
        #JSESSIONID=F92C175A6CA7FD502756FAF42717883E
        #Cookie: JSESSIONID=E94098397DCAE737FB275E0FCE3C75AC; tk=AtdhC6m_U6Kjoq0at5QgEY6nmeDQDUNz_4Kb7Stw2AEjnp1p0; RAIL_EXPIRATION=1571151791595; RAIL_DEVICEID=mPUVPyCHB4hb8j1gPVjkMB2n-g6r8wzx7HuGL-OAfLFHQ_zGZf2lmhWlXDh1OcZF9KzmSG-Ry-TItS0Du9I7rUS4wlvh07csdnz4rz9sEawcwqTl24j3x8Kz3Mxe8HW3mZte2aQ6Y2DwWtU580hCEN3MnRwnyk_U; BIGipServerotn=451936778.38945.0000; BIGipServerpool_passport=166527498.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; ten_key=Kt8ocm0TifWJ6Vx8WIl3ZEJ/itZUXFZU; ten_js_key=Kt8ocm0TifWJ6Vx8WIl3ZEJ%2FitZUXFZU
        print(cls.session.cookies)
        print("")

    @classmethod
    def init(cls):
        print("init")
        response = cls.session.get(URL.init_url)
#         with open("yzm.jpg","wb") as f:
#             f.write(response.content)
        #print(response.content)
        html_text_lines = response.content.decode().split('\n')
        for line in html_text_lines:
            print(line)
        
        print("")
#         print(response.json)
#         print("")
    @classmethod
    def query_myorder(cls):
        print("query_myorder")
        data_dict = { "come_from_flag": "my_order",
                            "pageIndex": 0,
                            "pageSize": 8,
                            "query_where": "H",
                            "queryStartDate": "2019-09-29",
                            "queryEndDate": "2019-10-14",
                            "queryType": 1,
                            "sequeue_train_name": ""

            }
        response = cls.session.post(URL.query_myorder_url,data_dict)
#         with open("yzm.jpg","wb") as f:
#             f.write(response.content)
        #print(response.content)
        print(response.json())

        
        print("")
    
    @classmethod
    def init_dc(cls):
        print("init_dc")
        data_dict = { "_json_att": ""
            }

        
        response = cls.session.post(URL.init_dc_url)
        
        html_text_lines = response.content.decode().split('\n')
        for line in html_text_lines:
            if "globalRepeatSubmitToken" in line:
                print(line)
                APITool.globalRepeatSubmitToken= line[line.find("'")+1:len(line) -2]
                print(APITool.globalRepeatSubmitToken)
         

        
        print("")
    @classmethod
    def query_ticket(cls):
        print("query_ticket")
        data_dict = { "leftTicketDTO.train_date": "2019-10-16",
                            "leftTicketDTO.from_station": "SHH",
                            "leftTicketDTO.to_station": "BJP",
                            "purpose_codes": "ADULT"
            }
        query_ticket_full_url = URL.query_ticket_url
        #for (i=0,i<= len(data_dict))
        
        response = cls.session.get("https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-10-16&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=BJP&purpose_codes=ADULT")
        #https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-10-16&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=BJP&purpose_codes=ADULT

#         with open("yzm.jpg","wb") as f:
#             f.write(response.content)
        #print(response.content)
        print(response.json())

        
        print("")
        


if __name__ == '__main__':

    APITool.download_yzm()
    APITool.init()
    #APITool.query_myorder()
    APITool.init_dc()
    APITool.query_ticket()
