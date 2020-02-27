import requests
from practical_01.data_package.cookie_package import LoginCookie
class HttpRequest:
    def request_api(self,method,url,data,cookie=None):
        header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        if(str.lower(method)=="get"):
            res = requests.get(url, data, headers=header,cookies=cookie)
            print(res.text)
        elif(str.lower(method)=="post"):
            res = requests.post(url, data, headers=header,cookies=cookie)
            print(res.text)
        return res

    def get_login_cookie(self):
        url="http://localhost:8000/enviroment_monitor/login.do"
        data={"account":"zhangsan","password":"zs1234"}
        header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        res = requests.get(url, data, headers=header)
        print(res.text)
        return res.cookies

# if __name__ == '__main__':
#     res = HttpRequest().get_login_cookie()
#     print(res)