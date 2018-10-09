import requests

post=requests.post('http://httpbin.org/post')
put=requests.put('http://httpbin.org/put')
delete=requests.delete('http://httpbin.org/delete')
head=requests.head('http://httpbin.org/get')
options=requests.options('http://httpbin.org/get')
print(post.text)
print(put.text)
print(delete.text)
print(head.text)
print(options)

