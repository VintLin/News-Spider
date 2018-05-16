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
 |    |-Web
 |       |-__init__.py
 |       |-news163com.py
 |       |-newscricn.py
 |       |-wwwfjsencom.py
 |       |-wwwsouthcncom.py
 |    
 |-Model
 |    |-__init__.py
 |    |-model.py
 |    
 |-vSQL
      |-db.json
      |-...
```
## 导入包:
```cmd
pip install pymysql
pip install BeautifulSoup4
pip install requests
```
#### 建议 :
##### 在阅读项目文档之前
##### 1.请先移步了解 [![vSQL](https://www.python.org)](https://www.python.org) 的项目文档。
##### 2.读者需要具有编写爬虫代码的经验(了解Re / BeautifulSoup库)。
##### 3.由于需要将各别信息存储在数据库中,所以请配置好mysql数据库。
## 如何使用:
_在这个项目中已经编写了4个分别爬取 网易新闻 / 国际在线 / 东南网 / 南方网 的示例。
所以在你配置好MySQL数据库,并在News-Spider/vSQL/db.json中填写相应的字段,
就可以直接运行News-Spider/Spider/Exec.py爬取网页了。_

