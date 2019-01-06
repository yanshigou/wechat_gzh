# encoding: utf-8
import requests
import re
import sys
import random
from time import sleep
import json
import xlrd
import sys
import xlwt
import urllib
from urllib import request

sep = '\n'
sep1 = '*'*50 + '\n'
sep2 = '\n' + '*'*50 + '\n\n'


Agent = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
         "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
         "Mozilla/5.0 "
         "(Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
         "Mozilla/5.0 "
         "(Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
         'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
         'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)',
         'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; '
         'MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
         'Mozilla/4.0 (compatible; MSIE 7.0; America Online Browser 1.1; Windows NT 5.1; (R1 1.5); '
         '.NET CLR 2.0.50727; InfoPath.1)',
         'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; '
         'FunWebProducts)',
         'Mozilla/5.0 (X11; U; UNICOS lcLinux; en-US) Gecko/20140730 (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
         'Mozilla/5.0 (X11; U; Linux; pt-PT) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.4'
         ]


# API = ['https://mp.weixin.qq.com/s?timestamp=1546583898&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-EPbq4cu-9Vw276hYTyTxhQl71kifxhqJ0VDFY28aCcFonZTPfw6F4Z0oCyLXnWs1GZztpCUi*iTPBdFfa*ugpfBQIXBdQ*rk0smZ9lZNzEDgpD7M42fv4YmYhSvUCDFFhJ*rdlVEH2Dyqn*smDAIUM=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgUzqR7kcigvPuXw5b2cUQHwDWc32NmQzITherJiV8opZ*6PUEYxX-jA-GPeflzKgQx67vZOMFPImFG6lMzHXKghk=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgUzeYq610hkGpg6tnUTs8JbvaCOzpPr6XsM3QJnVZTe8tGDcT-WGvCKhch-mJr80YIS2Fwzi81tKmdwmm*VKMbpo=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgUxIFByjMrXcnqrzBD8UlRI9YpCfSnKyU8LgvhN5tDb1GuiyRLsQ-yyu499Y6Q6HmN5lwdMIM82MHtwHHP61J3SE=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgU9ZAJcndtrQuNJjKCj1SqcNKX1c*bdStOm-cTpmz7DWX7srYRfv7ZGTf5NAWlcG9TQ9xv1TOLB8JTV1nUD-PYFQ=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgU8qb6Jiw-WZhP2S0LqzH4XKwlgOCoz3kkRKqmqB3T-FTHg5HmcFMda0ZhsYgIFEo*NGLB8*ti5eq1EpU*uBTw-0=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgUx1UCLskxjO-WfD-W0bqaNk8-gb-WAOcRh7lf2Li6FC4BbzlOMLka8aYI5O3Ay-1svvsXUHYC4FjVHCvMeHC46Q=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgUx1UCLskxjO-WfD-W0bqaNkGEebpyyz8Zlo0Av2JI5u7w2oykJwCIuPkzn3ARmA21R8qiGEDALM7LENA61KnLnY=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgU*6sakHYs2VU*CNEPFGcCg*tnJruHeIIpo1uscx57d7lmB173W2Ms5fipOakpmvAhWyiMQ0kYRnH17n2Jv9WT9o=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgU*6sakHYs2VU*CNEPFGcCg9Vqn7*6y4lf1mnMTkmuqlfEkkpI5F42zq3niH5ObCtAa5-PnE230bevITvHx5lUDY=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgU7nvM78G-xsSbs33BYp0-LljvjgF6St4tDSIfbwu3yiUtPvK2Ro9Xrze71UmO1cuQ*FBIdq23rSOjY5gsHooSlA=',
#         'https://mp.weixin.qq.com/s?timestamp=1546586843&src=3&ver=1&signature=3HJXlsmmaMAvR8LiIMWH-PVPyB250MvOQghlIjdq6zliVG0tnAENFVygisj7O8Nh*C6riZ6oOBJ9A4srESDgUwMUxk9MrSzsfac22ZCf4*bDdQVnYQT69mRyO3bYcD7Tce5hiEthSu0aeQ7EYjDNVGTII3LUyvP33yx6go7BKko='
#         'https://mp.weixin.qq.com/s/Tg97pbcPTxt9Ts5D4GDs9g'
#         'https://mp.weixin.qq.com/s/Gh9r6JeZb_Z4Fp54PCoygA',



# begin 从0-125 每一页增加5
# Request_URL = 'https://mp.weixin.qq.com/cgi-bin/appmsg?token=118126570&lang=zh_CN&f=json&ajax=1&random=0.4320727522988903&action=list_ex&begin=0&count=5&query=&fakeid=MzUyMTc1ODU5OQ%3D%3D&type=9'
Request_URL = 'https://mp.weixin.qq.com/cgi-bin/appmsg?token=118126570&lang=zh_CN&f=json&ajax=1&random=0.734833606349133&action=list_ex&begin=0&count=5&query=%E4%BB%8A%E6%97%A5%E5%A5%B3%E7%A5%9E&fakeid=MzUyMTc1ODU5OQ%3D%3D&type=9'

filename = 'C:\\Users\\shenz\\Desktop\\爬取公众号图片\\json.txt'

def randomAgent():
    headers = {'User-Agent': random.choice(Agent)}
    # print(headers)
    return headers


def get_link(filename):
    API2 = []
    f = open(filename)
    for each in f:
        # "link": "http://mp.weixin.qq.com/s?__biz=MzUyMTc1ODU5OQ==&mid=2247484065&idx=1&sn=af88f912c6691cf1738eb8975d2bd8bd&chksm=f9d77049cea0f95f22b5d46d09332f3cc6373e592c7d367e750e61f2e3f774cc8d21f83fcfd6#rd"
        link = re.findall(r'http://.*?#rd', str(each), re.S)
        # print(link)
        for i in link:
            API2.append(i)

    return API2

def get_api(Request_URL):
    headers = randomAgent()
    res = requests.get(Request_URL, headers=headers).content
    res = json.loads(res)
    print(res)


def xiazai(API2):
    imgName = 0
    for API in API2:
        headers = randomAgent()
        res = requests.get(API, headers=headers)
        # res = requests.get(API, headers=headers)
        # print(res.text)

        result = re.findall(r'data-src=".*?"', res.text, re.S)

        for i in result:
            try:
                url = i.split('"')[1]
                print(url)
                # f = open('C:\\Users\\shenz\\Desktop\\爬取公众号图片\\' + str(imgName) + ".jpg", 'wb')
                # f.write(requests.get(url, headers=headers).content)
                urllib.request.urlretrieve(url, '%s.jpg' % imgName)
                # f.close()
            except Exception as e:
                print(e)
                print(imgName, " error")
            imgName += 1


if __name__ == '__main__':
    API2 = get_link(filename)
    xiazai(API2)
    # get_api(Request_URL)
