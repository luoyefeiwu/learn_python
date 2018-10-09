import http.cookiejar, urllib.request

# 1.生成cookies
#filename='cookes.txt'
#cookie=http.cookiejar.LWPCookieJar(filename)
#cookie=http.cookiejar.MozillaCookieJar(filename)
#cookie = http.cookiejar.CookieJar()
# cookie.load('cookes.txt',ignore_discard=True,ignpre_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

# 2.加载cookies

cookie=http.cookiejar.LWPCookieJar()
cookie.load('cookes.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))

