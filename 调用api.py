import requests
response= requests.get("https://v1.hitokoto.cn/")   #调用名言网站
f = response.json()     #得到json文件，本质是个字典
a = f["hitokoto"]       #从字典中提取hitokoto这个值，提取到的也就是名言了
print(a)