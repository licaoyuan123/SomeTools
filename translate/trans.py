#coding: utf-8 
# auther: neutronest
'''
fanyi.youdao.com/openapi.do?keyfrom=neutronest-blog&key=1373749244&type=data&doctype=<doctype>&version=1.1&q=your word
'''

import sys
import requests
import httplib
import urllib
import urllib2
import json
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

def web_result(json_data):
    data = json.loads(json_data)
    if data == "":
        return
    web_trans = {}
    web_data = data.get('web')
    if web_data == None:
        return "没有拓展词义"
    for item in web_data:
        web_trans[item.get('key')] = item.get('value')
    return json.dumps(web_trans,ensure_ascii=False)

if __name__ == '__main__':
	 while True:
	 	s = raw_input('please input the word you wantto translate>>> ')
                # keyfrom=neutronest-blog&key=1373749244&type=data&doctype=<doctype>&version=1.1&q=your word
                params = {}
                params['keyfrom'] = 'neutronest-blog'
                params['key'] = '1373749244'
                params['type'] = 'data'
                params['doctype'] = 'json'
                params['version'] = '1.1'
                params['q'] = s

                # check the input
                if s == ":cl":
                    print "clean screen"
                    for i in range(1,30):
                        print "\n"
                    continue
                if s == ":q":
                    exit()
                try:
                    data = urllib.urlencode(params)
                    req = urllib2.Request(INIT_URL,data)
                    res = urllib2.urlopen(req)
                    data = res.read()
                    print '<<<','基本词义:', basic_result(data)
                    print '<<<','拓展词义:', web_result(data)
                except:
                    print "some error happened"
