#!/opt/local/bin/python
"""
Author: Pion Qiu
Description: file content
Date: 2023-04-19 20:45
LastEditors: Pion Qiu
LastEditTime: 2023-04-19 20:45

"""

import json
import os
import time
import requests
import subprocess
import datetime 

os.environ["AUTO_NET_RECONNECT_LOG_FILE"] = "～/Desktop/connect.log" #log文件路径

def log(info):
    log_file = os.environ.get("AUTO_NET_RECONNECT_LOG_FILE", "connect.log")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间并格式化
    log_info = f"{now} {info.strip()}"
    print(log_info)
    with open(log_file, "a") as f:
        f.write(log_info + "\n")


def login():
    url = "http://192.168.50.3:8080/eportal/InterFace.do?method=login"
    # config_file = os.environ.get('AUTO_NET_RECONNECT_CONFIG_FILE', "content")
    # with open(config_file, "r") as f:
    #     data = f.read().strip('"').strip("'")
    # header = {
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    # }

    # 以下信息需要自己抓包
    # <------将抓包得到的headers内容填写到键值对中------>
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "879",  # 填写抓包得到的值
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "",  # 填写抓包得到的cookie
        "Host": "192.168.50.3:8080",  # 填写抓包得到的host
        "Origin": "http://192.168.50.3:8080",  # 填写抓包得到的origin
        "Pragma": "no-cache",
        "Referer": "",  # 填写抓包得到的referer
    }
    # <------headers结束------>

    # <------将抓包得到的载荷内容填写到键值对中------>
    data = {
        "userId": "",  # 填写抓包得到的userId
        "password": "",  # 填写抓包得到的password
        "service": "",  # 填写抓包得到的service
        "queryString": "",# 填写抓包得到的queryString
        "operatorPwd": "",
        "operatorUserId": "",
        "validcode": "",
        "passwordEncrypt": "true",  # 填写抓包得到的passwordEncrypt
    }
    # <------载荷结束------>

    try:
        response = requests.post(url, data, headers=headers, timeout=10)
        content = json.loads(response.text)
        encoding = response.encoding
        if content["result"] == "fail":
            msg = content["message"].encode(encoding).decode("utf-8")
            log(msg)
            if msg == "认证设备响应超时,请稍后再试!":
                time.sleep(120)
            if msg == "正常上网时段为:日常06:00-23:59，请在以上时段内进行认证上网!":
                time.sleep(1200)
            if msg == "用户上线不超过10s，不允许抢占!":
                time.sleep(30)
        else:
            log("login at --> " + time.asctime(time.localtime(time.time())))
        return
    except Exception as info:
        log("login 连接异常:" + str(info))



def check_internet():
    """
    检查是否有互联网连接
    :return: True表示有互联网连接，False表示没有
    """
    try:
        url = "http://www.aliyun.com"
        # 使用curl获取HTTP头信息，并筛选包含Content-Length关键字的行
        cmd = ["curl", "-sI", url, "|", "grep", "Content-Length", "|", "awk", "-F': '", "'{print $2}'"]
        output = subprocess.check_output(" ".join(cmd), shell=True)
        Content_Length = output.decode().strip()
        if Content_Length == '500':#未认证时curl待测url地址会重定向到认证页面，已知认证页面HTTP头信息中Content-Length为500，若为其他值则认为已认证
            return False
        else:
            return True
    except Exception:
        return False

if __name__ == "__main__":
    while True:
        if check_internet():
            #print('connected')#测试使用
            time.sleep(1)
        else:
            #print('not connected')#测试使用
            login()
            time.sleep(1)            

