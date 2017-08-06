#encoding=utf-8
import json
import os
import time
# 练习3
# 密码修改：http://127.0.0.1:80/updatePwd?token=12343&telephone=18600001111&newPwd=1234
# 接口的类型：put
#注册方法
filePath = "register.txt"

#判断用户是否存在
def userExist(userName,userPwd):
    flag = 0 #0表示不存在
    if os.path.exists(filePath) == False:
        with open(filePath,"w") as f:
            f.write("")
    if os.path.exists(filePath):
        with open(filePath,"r") as f:
            lines = f.readlines()
            for line in lines:
                # if(line.startswith(userName+','+userPwd)):
                if (line.startswith(userName)):
                    flag = 1 #表示存在
                    break
    return flag
#注册方法
def regigercCheck(userName,userPwd):
    #判断用户是否存在
    flag = userExist(userName,userPwd)
    if flag == 0:#用户不存在的情况
        with open(filePath,"a+") as f:
            f.write("\n"+userName+","+userPwd)
        # return json.loads('{"message":"user register success","status":0}') #或者使用下面的选项
        return {"message":"user register success","status":0}
    else: #用户存在的情况
        return {"message":"user has registered,user name is '+userName+'","status":1}

def loginCheck(userName,userPwd):
    flag = userExist(userName,userPwd)
    if flag == 0:
        return json.loads('{"message":"user is not exist ' + userName + '","status":1}')
    else:
        ##如果用户名正确，则追加写token
        with open(filePath,"a+") as f:
            token = "testtoken"
            timestamp = time.time()
            f.write("\n" + userName + "," + userPwd +"," + token)
        return  {"message":"user login success","status":0,"token":token,"timestamp":timestamp}

def updatepswCheck(userName,userPwd,token):
    flag = userExist(userName,userPwd)
    timestamp = time.time()
    if flag == 0:
        return json.loads('{"message":"user is not exist ' + userName + '","status":1}')
    else:
        with open(filePath,"a+") as f:
            if token == "testtoken":
                f.write("\n" + userName + "," + userPwd + "," + token)
                return  {"message":"userpsw update success","status":0,"token":token,"timestamp":timestamp}
            else:
                return {"message": "userpsw update fail", "status": -1, "timestamp": timestamp}