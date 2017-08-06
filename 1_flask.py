# encoding=utf-8
from flask import Flask,request,make_response,jsonify,send_file,Response
import random
from openpyxl import load_workbook,Workbook
import Common
import os
#实例化应用
app = Flask(__name__)
#配置应用(接口)
#测试
@app.route("/login",methods=["GET","POST"])
def login():#定义一个方法
    #获取参数
    userName = request.args.get("userName")
    userPSW = request.args.get("userPSW")
    result = Common.loginCheck(userName,userPSW)
    return jsonify({"result": result})

@app.route("/sign",methods=["POST"])
def sign():
    userName = request.args.get("userName")
    userPSW = request.args.get("userPSW")
    result = Common.regigercCheck(userName,userPSW)
    return jsonify({"result": result})

@app.route("/updatePwd",methods=["PUT"])
# http://127.0.0.1:80/updatePwd?token=12343&telephone=18600001111&newPwd=1234
def updatePwd():
    userName = request.args.get("userName")
    newPwd = request.args.get("newPwd")
    token = request.args.get("token")
    result = Common.updatepswCheck(userName,newPwd,token)
    return jsonify({"result": result})

@app.route("/getCookies",methods=["GET","PUT","option"])
def testCookies():
    #自定义请求
    mr = make_response(jsonify({"message":"getCookies sucess"}))
    mr.set_cookie("cookiesName","cookiesValue")
    return mr

@app.route("/getMyParams",methods=["GET","option"])
def getMyParams():
    #获取参数url:http://127.0.0.1:8888/getMyParams?param1=param11&param1=param11
    url = str(request.url)
    #字符串切割[起始位置：]
    url = url[url.find("?")+1:]
    #使用split进行切割
    urlList = url.split("&")
    #使用循环去遍历
    for i in range(len(urlList)):
        value = urlList[i]
        print value.split("=")[1]
    print "second:",urlList
    print "first:",url
    param1 = request.args.get("param1") #获取参数
    param2 = request.args.get("param2")
    param3 = request.args.get("param2")
    return  jsonify({"result":"success"})

@app.route("/upload",methods=["POST"])
def upload():
    data = request.form
    print data
    # file = request.files["filename"]
    # file.save("client.txt")
    #服务端的哈希校验（hash）----文件传到服务端
    files  = request.files
    for i,j in files.items():
        j.save("%s,test.txt"%i)
    return  jsonify({"message":"upload seccess","data":data})

@app.route("/download",methods=["GET"])
def download():
    # 读文件名称
    fileName = request.args.get("filename1")
    # 构造相应的返回消息
    file = send_file(os.getcwd()+"\\"+fileName)
    print file
    response = make_response(file)  # 自定义响应
    return response  # 返回自定义响应

@app.route("/download2",methods=["get"])
def download2():
    #读文件名称
    fileName = request.args.get("fileName")
    #构造相应的返回消息
    file = send_file(os.getcwd()+"\\"+fileName)
    response = make_response(file)#自定义响应
    return response #返回自定义响应

@app.route("/downloadStream",methods=["Get"])
def downloadStream():
    #读文件名称
    fileName = request.args.get("fileName")
    #获取文件流
    fp = open(os.getcwd()+"\\"+fileName,"rb")
    response = Response(fp.read())#自定义响应
    return response #返回自定义响应

#定义异常
class MyEception(Exception):
    def __init__(self,message):
        self.message=message
    def returnMessage(self):
        return {"message":self.message}

#触发异常：2. 将一场加载到errorhandle中
@app.errorhandler(MyEception)
def tesMYerror(myEception):
    #获取异常结果
    return jsonify(myEception.returnMessage())
#3.触发异常
@app.route("/testMyException",methods=["post"])
def testMyException():
    raise MyEception("test test myEception ")

@app.route("/testMethod",methods=["get"])
def testMethod():
    method =request.method
    if method== "GET":
        print "GET"
    else:
        print method
    return jsonify(method)

@app.route("/testPath/<path>",methods=["post","put"])
def testPath(path):
    message = ""
    if path == "path1":
        message = "path1"
    elif path == "path2":
        message = "path2"
    return  jsonify({"message":message})


if __name__ =='__main__':
   app.run(host='127.0.0.1',port=8888,debug=True)