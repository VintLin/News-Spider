# News-Spider
## Version : v011
##### News-Spider项目是用于爬取网页新闻的小型爬虫框架。
[![News-Spider](https://github.com/VoterLin/News-Spider)](https://github.com/VoterLin/News-Spider)
[![vSQL](https://www.python.org)](https://www.python.org)
[![Python3.7](https://pypi.python.org/pypi/pubnub/)](https://pypi.python.org/pypi/pubnub/)
## 项目结构:
```python
 News-Spider
 |-Spider
 |    |-__init__.py
 |    |-Exec.py
 |    |-SpiderTool.py
 |    |-Website.py
 |    |_Web
 |       |-__init__.py
 |       |-news163com.py
 |       |-newscricn.py
 |       |-wwwfjsencom.py
 |       |_wwwsouthcncom.py
 |    
 |-Model
 |    |-__init__.py
 |    |_model.py
 |    
 |-vSQL(是一个简单的关系型数据库框架)
      |-db.json
      |_...
```
## 导入包:
```cmd
pip install pymysql
pip install BeautifulSoup4
pip install requests
```
#### 建议 :
###### 在阅读项目文档之前
 1.请先移步了解 [![vSQL](https://www.python.org)](https://www.python.org) 的项目文档。<br />
 2.读者需要具有编写爬虫代码的经验(了解Re / BeautifulSoup库)。<br />
 3.由于需要将各别信息存储在数据库中,所以请配置好MySQL数据库。
## 如何使用:
_在这个项目中已经编写了4个分别爬取 网易新闻 / 国际在线 / 东南网 / 南方网 的示例。_
### 1.填写db.json
配置好MySQL后(推荐使用[![Front](http://www.mysqlfront.de/)]管理你的数据库)<br />
打开News-Spider/vSQL/db.json
```json
{"HOST": "<主机名>", "USER": "<用户名>", "PWD": "<密码>", "DB": "<数据库名>"}
```
将其中由"<>"括起的，替换为相应字段。
### 2.运行Exec.py
直接运行News-Spider/Spider/Exec.py爬取网页。

## 爬取的数据
_爬取的页面会被存储为*.html文件保存在News-Spider/Spider/page文件夹中<br />，
以及该页面中新闻的一些标识信息(如:发布时间，标题...)将被存储到数据库中_
### 1.page文件夹
在执行Exec.py后将在 News-Spider/Spider/ 目录下创建一个page文件夹用于存放新闻页面。<br />
并以如下格式创建路径:
```shell
/page/<新闻类型>/<新闻发布时间>/<文件名>
```
例如:http://home.163.com/18/0514/11/DHP0NGKO00108O8H.html <br />
该新闻页面将被存储的路径为：
```shell
/page/家居/2018-05-14/DHP0NGKO00108O8H.html
```
### 2.数据库中的News表
同样是执行Exec.py后，通过使用vSQL在MySQL数据库中创建一张名为News的表。</br>
保存如下字段:
```sql
字段           类型              说明
id            int(20)           主键，自增
filename      char(80)          文件名
path          char(100)         在page目录下的路径
website       char(20)          来源网站
title         char(80)          新闻标题
time          datetime          新闻发布时间
type          char(20)          新闻类型
```
例如:http://home.163.com/18/0514/11/DHP0NGKO00108O8H.html <br />
该新闻页面被爬取后获得的相应字段如下：
```sql
字段           相应值
id            x (x为int类型,数据库中存储的第x行)
filename      DHP0NGKO00108O8H.html
path          /page/家居/2018-05-14/DHP0NGKO00108O8H.html
website       home.163.com
title         陈连武新作 | 丝旅之路，复兴东方神韵
time          2018-05-14 11:50:41
type          家居
```
