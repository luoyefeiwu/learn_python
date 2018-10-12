# url初始化
from pyquery import PyQuery as pq
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8
doc=pq(url='http://www.baidu.com')
print(doc('title'))
