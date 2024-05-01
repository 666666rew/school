from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)


soup = BeautifulSoup(html, features='lxml')
print(soup.h1)

"""
<h1>爬虫测试1</h1>
"""

print('\n', soup.p)

"""
<p>
        这是一个在 <a href="https://mofanpy.com/">莫烦Python</a>
<a href="https://mofanpy.com/tutorials/scraping">爬虫教程</a> 中的简单测试.
    </p>
"""

"""
<a href="https://mofanpy.com/tutorials/scraping">爬虫教程</a>
"""

all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)

