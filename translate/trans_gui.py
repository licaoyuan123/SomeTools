
# coding: utf-8
# auther: Loveice && neutronest
# 

import sys
import requests
import httplib
import urllib
import urllib2
import json
from Tkinter import *
reload(sys)
sys.setdefaultencoding('utf-8')
INIT_URL = 'http://fanyi.youdao.com/openapi.do'

# format: {"translation":["分布"],"basic":{"phonetic":"dɪstrɪ'bjuːʃ(ə)n","explains":["n. 分布；分配"]},"query":"distribution","errorCode":0,"web":[{"value":["分配","分布","配送"],"key":"Distribution"},{"value":["二项分布","二项分配","二项式分布"],"key":"Binomial distribution"},{"value":["均匀分布","均匀分配","连续型均匀分布"],"key":"Uniform distribution"}]}
def basic_result(json_data):
    data = json.loads(json_data)
    if data == "":
        return
    if data.get('basic') == None:
        return "没有基本词义"
    basic_trans = data.get('basic')
    basic_explain = basic_trans.get('explains')
    return json.dumps(basic_explain,ensure_ascii=False)

def callback():
	params = {}
	params['keyfrom'] = 'neutronest-blog'
	params['key'] = '1373749244'
	params['type'] = 'data'
	params['doctype'] = 'json'
	params['version'] = '1.1'
	params['q'] = v1.get()
	data = urllib.urlencode(params)
	req = urllib2.Request(INIT_URL,data)
	res = urllib2.urlopen(req)
	data = res.read()
	showresult(data)

def showresult(data):
	v2.set(basic_result(data))

win = Tk()  #
win.title('词典贺岁版')
win.geometry('400x200')

Label(win, text="要查的词", font ="16", width=30, height=2, wraplength=80).pack()
v1 = StringVar()
v2 = StringVar()
Entry(win, width = 30, textvariable = v1).pack()
Button(win, text = "查找", bd=2, font = "15", width=15, command=callback).pack()
Entry(win, width = 60,  textvariable = v2).pack()


mainloop()