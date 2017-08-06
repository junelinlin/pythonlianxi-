#encoding=utf-8
#编写用户注册的场景
#1、服务端：注册成功的返回响应（json）
#2、客户端：进行访问
#
import requests
import os

def sign(userName,userPSW):
    data = {"userName":userName,"userPSW":userPSW}
    url= "http://127.0.0.1:8888/sign"
    res = requests.post(url=url,params=data)
    return res

def login(userName,userPSW):
    data1 = {"userName":userName,"userPSW":userPSW}
    url1= "http://127.0.0.1:8888/login"
    res1 = requests.get(url=url1,params=data1)
    return res1

def updatePwd(userName,newPwd,token):
    data1 ={"userName": userName, "newPwd": newPwd,"token":token}
    url1 = "http://127.0.0.1:8888/updatePwd"
    res = requests.put(url=url1,params=data1)
    return res

def testCookies():
    #发送消息
    res = requests.get("http://127.0.0.1:8888/getCookies")
    #获取cookies
    cookies = res.cookies
    value = cookies.get("cookiesName")#通过get获取
    print value
    print res.text
    # 将CookieJar转为字典：
    cookies1 = requests.utils.dict_from_cookiejar(res.cookies)
    print cookies1
    print res.cookies
    print res.headers

def testMyParams():
    params = {"param1":["param11","param11"]}
    res = requests.get("http://127.0.0.1:8888/getMyParams",params=params)
    print res.text

def  testUpload():
    f1 = open("register.txt","rb")
    f2 = open("register.txt", "rb")
    files = {"filename1":f1,"filename2":f2}
    data = {"data1":"testdata","data2":"datavalue2"}
    res = requests.post("http://127.0.0.1:8888/upload",files = files,data=data)
    print res.text

def testDownload():
    #指定文件名称
    fileName = "register.txt"
    filename= {"filename1":fileName}
    #发送响应
    res = requests.get("http://127.0.0.1:8888/download",params=filename)
    return res.content

def testDownload2():
    #指定文件名称
    fileName ="register.txt"
    params = {"fileName":fileName} #使用params传参
    #发送响应
    # res = requests.get("http://127.0.0.1:8888/download?fileName="+fileName)
    res = requests.get("http://127.0.0.1:8888/download2",params=params)
    #得到响应内容,并写入文件中
    with open(os.getcwd()+"\\downloadtest1.png","wb") as f:
        f.write(res.content)

def testDownloadSteam():
    fileName = "register.txt"
    file = {"fileName":fileName}
    res= requests.get("http://127.0.0.1:8888/downloadStream",params=file)
    with open("DownloadStr.txt","wb") as fp:
        fp.write(res.content)

def testmyEception():
    res = requests.post("http://127.0.0.1:8888/testMyException")
    return res.text

def testMethod():
    res = requests.get("http://127.0.0.1:8888/testMethod")
    return res.text

def testPath():
    res = requests.put("http://127.0.0.1:8888/testPath/path2")
    return res.text

if __name__ == "__main__":
    # print sign("123456","123")
    # print sign("123456","123")
    # print login("123456","123")
    # print login("123456789", "123")
    # r =  updatePwd("123456", "123newpsw",'111')
    # testCookies()
    # testUpload()
    # testDownloadSteam()
    print testmyEception()
    print testMethod()
    print testPath()

