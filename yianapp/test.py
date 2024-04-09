import json

import requests

# API的URL
url = 'http://172.26.78.203:8080/agvapi/carsInformation'

# 准备请求头，如果需要的话，可以添加认证信息或其他头部
headers = {
    'Content-Type': 'application/json',  # 告知服务器发送的是JSON格式数据
}

# 因为没有提供需要发送的数据，所以请求体为空
data = {}

# 发送POST请求
response = requests.post(url, headers=headers, json=data)
print("触发了吗？")

# 检查请求是否成功
if response.status_code == 200:
    # 解析返回的JSON数据
    result = response.json()
    print("是滚筒的呀!", result)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # 打印返回的错误信息

