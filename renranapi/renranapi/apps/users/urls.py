from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    # path("captcha/", views.CaptchaAPIView.as_view()),
    path("", views.UserCreateAPIView.as_view()),
]