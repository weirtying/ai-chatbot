import requests
messages = []
while True:
    attend = input()
    messages.append({"role": "user", "content": attend})
    response= requests.post("https://api.deepseek.com/v1/chat/completions",     #调用deepseek模型的api
                            headers={"Authorization": "Bearer sk-*******************"},    #输入你的api密钥
                            json={ "model": "deepseek-v4-pro",      #选择模型
                                   "messages": messages     #输入你的话
                                 }
                            )
    if attend == "退出":
            break
    a = response.json()     #得到一大堆返回的数据
    b = a["choices"][0]     #choices是一个列表，所有得多加一步选择元素，这里我们要的数据在0号元素
    c = b["message"]        #类似字典取值
    d = c["content"]
    messages.append({"role": "assistant", "content": d})
    print(d)
