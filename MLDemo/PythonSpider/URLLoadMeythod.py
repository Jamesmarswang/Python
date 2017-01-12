# coding = utf-8
# __author__ = 'wang wei'

import urllib.request
import urllib
import http.cookiejar

from bs4 import BeautifulSoup

url = "http://www.baidu.com"
print("---第一种方法---")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("---第二种方法---")
req = urllib.request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))

print("---第三种方法---")
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
# print(cj)
print(len(response3.read()))

html_doc = """
   </html>
	<head>
	<title>我的第一个网站</title>
	</head>
	<body>
	<p>哇！这是我的第一个网站。</p>
	</body>
	</html>
"""
soup = BeautifulSoup(html_doc, 'html.parse', from_encoding='utf-8')
print("获取所有连接")
links = soup.find_all('p')
