# Create your views here.
from rest_framework.views import APIView
from django.conf import settings
import json
from urllib.parse import urlencode
from urllib.request import urlopen
from rest_framework.response import Response
from rest_framework import status


class CaptchaAPIView(APIView):
    def get(self,request):
        """验证码的验证结果校验"""
        AppSecretKey = settings.TENCENT_CAPTCHA["App_Secret_Key"]
        appid = settings.TENCENT_CAPTCHA["APPID"]
        Ticket = request.query_params.get("ticket")
        Randstr = request.query_params.get("randstr")
        UserIP = request._request.META.get("REMOTE_ADDR")
        print("用户ID地址：%s" % UserIP)
        params = {
            "aid": appid,
            "AppSecretKey": AppSecretKey,
            "Ticket": Ticket,
            "Randstr": Randstr,
            "UserIP": UserIP
        }
        params = urlencode(params)

        f = urlopen("%s?%s" % (settings.TENCENT_CAPTCHA["GATEWAY"], params))
        content = f.read()
        res = json.loads(content)
        print(res)
        if res:
            error_code = res["response"]
            if int(error_code) == 1:
                return Response("验证通过！")
            else:
                return Response("验证失败！%s" % res["err_msg"], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("验证失败！", status=status.HTTP_400_BAD_REQUEST)