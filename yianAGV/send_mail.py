import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'yianAGV.settings'


# ['Dale_Tian@pegatroncorp.com', 'Lianchao_Yu@pegatroncorp.com'],
def mail(agvid, type, error, site):
    send_mail(
        'AGV异常',
        'Dear sir or Lady\n\n'+'  AGVID：'+agvid+'；AGV类型：' + type+'；异常信息：' + error+'；AGV目前停靠位置：' + site+'\n请尽快前往处理'+'\n\nThanks',
        'Dale_Tian@pegatroncorp.com',
        ['Dale_Tian@pegatroncorp.com', 'Lianchao_Yu@pegatroncorp.com'],
        fail_silently=False,
    )

# if __name__ == '__main__':
#     send_mail(
#         '来自小狐狸的邮件',
#         '这里是正文',
#         'Dale_Tian@pegatroncorp.com',
#         ['Dale_Tian@pegatroncorp.com'],
#         fail_silently=False,
#     )
