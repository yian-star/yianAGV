"""yianAGV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import yianapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', yianapp.views.index, name='index'),  # 直接进入到首页，不用在地址里输入index了
    path('agvlink/', yianapp.views.agvlink, name='agvlink'),
    path('stock_link/', yianapp.views.stock_link, name='stock_link'),
    path('smt_link/', yianapp.views.smt_link, name='smt_link'),
    path('agv_monitor/', yianapp.views.agv_monitor, name='agv_monitor'),
    path('plot_graph/', yianapp.views.plot_graph, name='plot_graph'),
    path('agv_route/', yianapp.views.agv_route, name='agv_route'),
    path('magnetism_agv_route/', yianapp.views.magnetism_agv_route, name='magnetism_agv_route'),
    path('magnetism_agv_route_sum/', yianapp.views.magnetism_agv_route_sum, name='magnetism_agv_route_sum'),
    path('test/', yianapp.views.test, name='test'),
    path('agv_route_sum/', yianapp.views.agv_route_sum, name='agv_route_sum'),
    path('roller_agv_sum/', yianapp.views.roller_agv_sum, name='roller_agv_sum'),
    path('roller_agv/', yianapp.views.roller_agv, name='roller_agv'),
    path('yian/', yianapp.views.yian, name='yian'),
]
