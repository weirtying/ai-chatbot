import requests
response= requests.post("https://api.deepseek.com/v1/chat/completions",     #调用deepseek模型的api
                        headers={"Authorization": "Bearer sk-7d20a47341d24f7d96bb0e2db807cd29"},    #输入你的api密钥
                        json={ "model": "deepseek-v4-pro",      #选择模型
                               "messages": [{"role": "user", "content": "你好"}]      #输入你的话
                             }
                        )
a = response.json()     #得到一大堆返回的数据
b = a["choices"][0]     #choices是一个列表，所有得多加一步选择元素，这里我们要的数据在0号元素
c = b["message"]        #类似字典取值
d = c["content"]
print(d)