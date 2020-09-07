from django.urls import path
from .views import home, about, contact, user_register, user_login, logout, account, username, otp_confirm, otp_verification, change_password, service

app_name = 'all'


urlpatterns = [
  path('',user_login,name='user-login'),
  path('logout/',logout,name='logout'),
  path('home/',home,name='home'),
  path('contact/',contact,name='contact'),
  path('about/',about,name='about'),
  path('register/',user_register,name='user-register'),
  path('account/',account,name='account'),

  path('username/',username,name="username"),
  path('otp_verification/<username>/',otp_verification,name="otp-verification"),
  path('change_password/',change_password,name="change-password"),
  path(r'otp/(?P<otp>\d+)/<user>/',otp_confirm,name="otp"),
  path('service/',service,name='service'),
]