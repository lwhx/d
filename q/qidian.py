# -*- coding: utf-8 -*-
# date：2021/12/13
 
from operator import gt
import requests
import json
import time
import random



'''
cookies = ""
# cookie转字典
def extract_cookies(cookies):
    global csrf
    cookies = dict([l.split("=", 1) for l in cookies.split("; ")])
    csrf = cookies['_csrfToken']
    return cookies
 
 
# 签到
def get1():
 cookie = extract_cookies(cookies)
 url = "https://my.qidian.com/ajax/Score/Receive?_csrfToken="+csrf+"&referObject=1"
 r = requests.get(url, cookies=cookie).text
 print(r)
 wxpusher(r)
 if r == '{\"code\":11608,"msg\":"不符合领取在线经验值的条件！\"}':
      print("签到过了")
      get2()
      if tk == '{\"code\":11608,"msg\":"不符合领取在线经验值的条件！\"}':
          print("签到过了")
          get3()
          if tk == '{\"code\":11608,"msg\":"不符合领取在线经验值的条件！\"}':
              print("签到过了")
              get4()
              if tk == '{\"code\":11608,"msg\":"不符合领取在线经验值的条件！\"}':
                  print("签到过了")
                  get5()
                  if tk == '{\"code\":11608,"msg\":"不符合领取在线经验值的条件！\"}':
                      print("签到过了")
                      get6()
                      if tk == '{\"code\":11608,"msg\":"不符合领取在线经验值的条件！\"}':
                          print("签到过了")
                          get7()
                          if tk == '{\"code\":11608,"msg\":"不符合领取在线经验值的条件！\"}':
                              get8()
                              print("签到完毕")
                          elif tk == '{\"code\":0,"msg\":"成功\"}':
                              print("第7次签到成功")
                              ys(61) 
                              get8()
                              print("签到完毕")
                      elif tk == '{\"code\":0,"msg\":"成功\"}':
                          print("第6次签到成功")
                          ys(61)
                          get7() 
                          ys(61)
                          get8()
                  elif tk == '{\"code\":0,"msg\":"成功\"}': 
                      print("第5次签到成功")
                      ys(31)                  
                      get6()                    
                      ys(61)
                      get7() 
                      ys(61)
                      get8()                       
              elif tk == '{\"code\":0,"msg\":"成功\"}':
                  print("第4次签到成功")
                  ys(31)
                  get5()
                  ys(61)
                  get6()
                  ys(61)
                  get7()
                  ys(61)
                  get8()                  
          elif tk == '{\"code\":0,"msg\":"成功\"}':
               print("第3次签到成功") 
               ys(21)
               get4()
               ys(31)
               get5()
               ys(61)
               get6()
               ys(61)
               get7()
               ys(61)
               get8()           
      elif tk == '{\"code\":0,"msg\":"成功\"}':
          print("第2次签到成功")
          ys(11)
          get3()
          ys(21)
          get4()
          ys(31)
          get5()
          ys(61)
          get6()
          ys(61)
          get7()
          ys(61)
          get8()
 #  elif r == '{\"code\":0,"msg\":"成功\"}':
      print("第1次签到成功")
      ys(6)
      get2()
      ys(11)
      get3()
      ys(21)
      get4()
      ys(31)
      get5()
      ys(61)
      get6()
      ys(61)
      get7()
      ys(61)
      get8()




 
## 开始执行... 2022-05-06 18:56:57

#{"code":11608,"msg":"不符合领取在线经验值的条件！"}
#{"code":0,"msg":"成功"}
 
def get2():
    global tk
    cookie = extract_cookies(cookies)
    url = "https://my.qidian.com/ajax/Score/Receive?_csrfToken="+csrf+"&referObject=2"
    tk = requests.get(url, cookies=cookie).text
    print(tk)
    wxpusher(tk)
   # return tk
   

def get3():
    cookie = extract_cookies(cookies)
    url = "https://my.qidian.com/ajax/Score/Receive?_csrfToken="+csrf+"&referObject=3"
    tk = requests.get(url, cookies=cookie).text
    print(tk)
    wxpusher(tk)
    
def get4():
    cookie = extract_cookies(cookies)
    url = "https://my.qidian.com/ajax/Score/Receive?_csrfToken="+csrf+"&referObject=4"
    tk  = requests.get(url, cookies=cookie).text
    print(tk)
    wxpusher(tk)

def get5():
    cookie = extract_cookies(cookies)
    url = "https://my.qidian.com/ajax/Score/Receive?_csrfToken="+csrf+"&referObject=5"
    tk = requests.get(url, cookies=cookie).text
    print(tk)
    wxpusher(tk)

def get6():
    cookie = extract_cookies(cookies)
    url = "https://my.qidian.com/ajax/Score/Receive?_csrfToken="+csrf+"&referObject=6"
    tk = requests.get(url, cookies=cookie).text
    print(tk)
    wxpusher(tk)

def get7():
    cookie = extract_cookies(cookies)
    url = "https://my.qidian.com/ajax/Score/Receive?_csrfToken="+csrf+"&referObject=7"
    tk = requests.get(url, cookies=cookie).text
    print(tk)
    wxpusher(tk)

def get8():
    cookie = extract_cookies(cookies)
    url = "https://my.qidian.com/ajax/Score/Receive?_csrfToken="+csrf+"&referObject=8"
    tk = requests.get(url, cookies=cookie).text
    print(tk)
    wxpusher(tk)

def wxpusher(msg):
   url01 = "http://wxpusher.zjiecode.com/api/send/message" 
   headers01 = {'Content-Type':'application/json'}
   data01 = {
            "appToken":"AT_M0lsJlJD1OOTcFsIHcRtLghRdKNfqZYN",
            "content":msg,
            "contentType":1,
            "uids":["UID_6kRbvvdaYLvlOsIDO2V4dOmlPsJb"]
            }

   requests.post(url=url01, data=json.dumps(data01), headers=headers01)


def ys(t):
    for i in range(t):
     time.sleep(60);
     print(i)
    


# 开启任务运行
#def run():
    #get1()
   

 
 
if __name__ == '__main__':
   # run()
   get1()
