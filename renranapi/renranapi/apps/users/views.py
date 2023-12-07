# Create your views here.
import random

from django_redis import get_redis_connection
from rest_framework.views import APIView
from django.conf import settings
import json
from urllib.parse import urlencode
from urllib.request import urlopen
from rest_framework.response import Response
from rest_framework import status


# class CaptchaAPIView(APIView):
#     def get(self, request):
#         """验证码的验证结果校验"""
#         AppSecretKey = settings.TENCENT_CAPTCHA["App_Secret_Key"]
#         appid = settings.TENCENT_CAPTCHA["APPID"]
#         Ticket = request.query_params.get("ticket")
#         Randstr = request.query_params.get("randstr")
#         UserIP = request._request.META.get("REMOTE_ADDR")
#         print("用户ID地址：%s" % UserIP)
#         params = {
#             "aid": appid,
#             "AppSecretKey": AppSecretKey,
#             "Ticket": Ticket,
#             "Randstr": Randstr,
#             "UserIP": UserIP
#         }
#         params = urlencode(params)
#
#         f = urlopen("%s?%s" % (settings.TENCENT_CAPTCHA["GATEWAY"], params))
#         content = f.read()
#         res = json.loads(content)
#         print(res)
#         if res:
#             error_code = res["response"]
#             if int(error_code) == 1:
#                 return Response("验证通过！")
#             else:
#                 return Response("验证失败！%s" % res["err_msg"], status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response("验证失败！", status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserModelSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


# class SMSCodeAPIView(APIView):
#     """
#     短信验证码
#     """
#     def get(self, request, mobile):
#         """
#         短信验证码
#         """
#         # 生成短信验证码
#         sms_code = "%06d" % random.randint(0, 999999)
#
#         # 保存短信验证码与发送记录
#         redis_conn = get_redis_connection('sms_code')
#         # 使用redis提供的管道操作可以一次性执行多条redis命令
#         pl = redis_conn.pipeline()
#         pl.multi()
#         pl.setex("sms_%s" % mobile, constants.SMS_CODE_EXPIRE, sms_code)   # 设置短信有效期为300s
#         pl.setex("sms_time_%s" % mobile, constants.SMS_CODE_INTERVAL, "_")    # 设置发送短信间隔为60s
#         pl.execute()
#
#         # 发送短信验证码
#         ccp = CCP()
#         ccp.send_template_sms(mobile, [sms_code, ], constants.SMS_CODE_EXPIRE//60, settings.SMS.SMS_TEMPLATE_ID)
#
#         return Response({"message": "OK"}, status.HTTP_200_OK)
