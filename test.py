'''
Created on 2019 10 9

@author: surface
'''

#from PyQt5.Qt import  *
import requests
from PyQt5.QtCore import QObject


class APITool(QObject):
    session = requests.session()
    
    @classmethod
    def download_yzm(cls):
        response = cls.session.get("https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand")
        with open("yzm.jpg","wb") as f:
            f.write(response.content)
        print(response.content)
        print(cls.session.cookies)


if __name__ == '__main__':
    print("aaa")
    APITool.download_yzm()
    print("bbb")