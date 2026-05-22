import requests     #打开requests库
response= requests.get("https://www.baidu.com")     #向百度发送get请求，返回到response这个变量里面
f= open("baidu.html","w")       #创建baidu.html这个文件写到f这个变量
f.write(response.text)      #把百度的响应放到上面那文件
f.close()       #关闭文件，保存文件
