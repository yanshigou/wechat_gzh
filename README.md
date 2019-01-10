# wechat_gzh

爬取微信公众号所有文章的图片



**主要是为了帮客户爬取某个公众号内的所有美女图片而写！！**

**并不知道具体用途！侵权联系删除！**



## 使用说明
1. 需要有[微信公众平台](https://mp.weixin.qq.com)的账号
2. 新建群发![](https://raw.githubusercontent.com/yanshigou/yanshigou.github.io/master/img/t/gzh1.png)
3. 自建图文![](https://raw.githubusercontent.com/yanshigou/yanshigou.github.io/master/img/t/gzh2.png)
4. 超链接![](https://raw.githubusercontent.com/yanshigou/yanshigou.github.io/master/img/t/gzh3.png)
5. 搜索公众号，再点击公众号进入搜索文章![](https://raw.githubusercontent.com/yanshigou/yanshigou.github.io/master/img/t/gzh4.png)
6. 在此页面使用F12查看Request URL和RequestHeaders![](https://raw.githubusercontent.com/yanshigou/yanshigou.github.io/master/img/t/gzh5.png)



* get_link(filename) 	是第一种版本 ，自己手动去调接口，复制json数据写入json.txt中，再进行分析下载
* get_api()                         为最新版本，只需要按我的步骤获取公众号的第一个Request URL，就能获取所有文章，并进行分析下载
* all_link.txt                      为每个文章的链接，顺便写出来的。



## 爬取结果

**仅为第一页，5篇文章的所有图片**

![](https://raw.githubusercontent.com/yanshigou/yanshigou.github.io/master/img/t/gzh6.png)