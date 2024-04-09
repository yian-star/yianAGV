import os

from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse, JsonResponse

# Create your views here.
from yianAGV import settings
from yianAGV.send_mail import mail
import requests


def index(request):
    return render(request, "user_login.html")
    # request.method--前台提交过来请求的方式
    # if request.method == 'GET':
    #     return render(request, "user_login.html")
    # elif request.method == "POST":
    #     # request.POST(相当于字典)--post形式提交过来的数据
    #     return render(request,"user_login.html")
    # request.POST.get("name")--推荐用get取值(取出列表最后一个值)
    # name = request.POST.get("name")
    # pwd = request.POST.get("pwd")
    # 连接数据库
    # conn = pymysql.connect(host="172.22.248.234", port=3306, ab="yianAGV")


def agvlink(request):
    return render(request, "templates/AGV3F.html")


def stock_link(request):
    return render(request, "PCBA_stock.html")


def smt_link(request):
    return render(request, "SMT.html")


def agv_monitor(request):
    return render(request, "templates/AgvMonitor.html")


def plot_graph(request):
    # 创建一个图形对象
    fig, ax = plt.subplots()

    # 绘制图形
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    ax.plot(x, y)

    # 保存图形为临时文件
    # temp_file = "/static/img/file.png"
    yian_file = settings.STATICFILES_DIRS[0]
    temp_file = os.path.join(yian_file, 'img')
    temp_file = temp_file + "\\file.png"
    plt.savefig(temp_file)

    # 读取临时文件的内容
    with open(temp_file, "rb") as file:
        image_data = file.read()

    # 返回图形的内容给HTML页面
    return HttpResponse(image_data, content_type="image/png")


# 顶升式的AGV数据
def agv_route(request):
    # http://172.26.93.63:8000/AllCarList
    import json

    import requests

    # 设置请求头和请求体
    headers = {'Content-Type': 'application/json'}
    data = {'key1': 'value1', 'key2': 'value2'}

    # 发送POST请求
    response = requests.post('http://172.26.93.63:8000/AllCarList', headers=headers, data=data)

    # 打印响应结果
    response_data = response.text

    agv_data_list = json.loads(response_data)  # 将字符串转换成Python列表list
    new_data = json.dumps(agv_data_list)  # 将Python列表转换成JSON字符串

    jacking_list = []
    for item in agv_data_list:
        if 'Type' in item and item['Type'] == 1:
            jacking_list.append(item)
    # 传的是list
    return JsonResponse({'data': jacking_list}, safe=False)


flagsite = -1


def agv_route_sum(request):
    global flagsite
    import json
    import requests

    # 设置请求头和请求体
    headers = {'Content-Type': 'application/json'}
    data = {'key1': 'value1', 'key2': 'value2'}

    # 发送POST请求
    response = requests.post('http://172.26.93.63:8000/AllCarList', headers=headers, data=data)

    # 打印响应结果
    response_data = response.text

    agv_data_list = json.loads(response_data)  # 将字符串转换成Python列表list
    new_data = json.dumps(agv_data_list)  # 将Python列表转换成JSON字符串

    jacking_list = []
    error_state = {'0': '待机停车', '1': '行驶中', '2': '急停触发', '3': '驱动器故障（磁）', '4': '脱线磁', '5': '满线磁', '6': '机械防撞触发磁',
                   '7': '光电避障传感器触发磁', '8': '电量不足磁', '9': '内部错误磁', '255': '未准备磁'}

    for item in agv_data_list:
        if 'Type' in item and item['Type'] == 1:
            jacking_list.append(item)
            if item['CurrState'] != 0 and item['CurrState'] != 1:
                agvid = str(item['AgvID'])
                agvtype = str(item['Type'])
                error = error_state[str(item['CurrState'])]
                site = str(item['CurrSite'])
                # 发送邮件给相关人员
                if flagsite != 0 and flagsite != int(item['CurrSite']):
                    flagsite = int(item['CurrSite'])
                    mail(agvid, '激光', error, site)
            # print('这里是总的顶升的AGV：', item)
    # 传的是list
    return JsonResponse({'data': jacking_list}, safe=False)


# 磁条AGV数据
def magnetism_agv_route(request):
    import json
    import requests
    # 设置请求头和请求体
    headers = {'Content-Type': 'application/json'}
    data = {'key1': 'value1', 'key2': 'value2'}
    # 发送POST请求
    response = requests.post('http://172.26.93.63:8000/AllCarList', headers=headers, data=data)
    response_data = response.text
    agv_data_list = json.loads(response_data)  # 将字符串转换成Python列表list
    magnetism_list = []
    for item in agv_data_list:
        if 'Type' in item and item['Type'] == 0:
            magnetism_list.append(item)
    # 传的是list
    print("磁条车子吗？：", magnetism_list)
    return JsonResponse({'magnetismdata': magnetism_list}, safe=False)


# 磁条AGV数据


magnetism_flagsite = -1


def magnetism_agv_route_sum(request):
    global magnetism_flagsite
    import json
    import requests
    # 设置请求头和请求体
    headers = {'Content-Type': 'application/json'}
    data = {'key1': 'value1', 'key2': 'value2'}
    # 发送POST请求
    response = requests.post('http://172.26.93.63:8000/AllCarList', headers=headers, data=data)
    response_data = response.text
    agv_data_list = json.loads(response_data)  # 将字符串转换成Python列表list
    magnetism_list = []
    error_state = {'0': '待机停车', '1': '行驶中', '2': '急停触发', '3': '驱动器故障（磁）', '4': '脱线磁', '5': '满线磁', '6': '机械防撞触发磁',
                   '7': '光电避障传感器触发磁', '8': '电量不足磁', '9': '内部错误磁', '255': '未准备磁'}

    for item in agv_data_list:
        if 'Type' in item and item['Type'] == 0:
            magnetism_list.append(item)
            if item['CurrState'] != 0 and item['CurrState'] != 1:
                agvid = str(item['AgvID'])
                error = error_state[str(item['CurrState'])]
                site = str(item['CurrSite'])
                # 发送邮件给相关人员
                if magnetism_flagsite != 0 and magnetism_flagsite != int(item['CurrSite']):
                    magnetism_flagsite = int(item['CurrSite'])
                    mail(agvid, '磁条', error, site)
    # 传的是list
    return JsonResponse({'magnetismdata': magnetism_list}, safe=False)


def test(request):
    return render(request, "templates/AGV1F.html")


roller_flagsite = -1


# 滚筒
def roller_agv_sum(request):
    global roller_flagsite
    import json
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
        result_data = result['data']
        for i in result_data:
            if int(i['runningState']) == 2:
                if roller_flagsite != 0 and roller_flagsite != int(i['currentPoint']):
                    agvid = str(i['carId'])
                    error = '故障'
                    site = str(i['currentPoint'])
                    roller_flagsite = int(i['currentPoint'])
                    mail(agvid, '滚筒', error, site)
        return JsonResponse({'rollerdata': result_data}, safe=False)
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)  # 打印返回的错误信息


def roller_agv(request):
    import json
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
        result_data = result['data']
        for i in result_data:
            print(i)
        return JsonResponse({'rollerdata': result_data}, safe=False)
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)  # 打印返回的错误信息


def yian(request):
    return render(request, "templates/yian.html")
