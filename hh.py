from urllib import request
url="http://baike.baidu.com/item/Android/60243"

response = request.urlopen(url)
print(response.read())