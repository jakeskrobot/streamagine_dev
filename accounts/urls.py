from django.conf.urls import url
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    url('', views.index, name='index'),
    url('login/', auth_login,  {'template_name': 'accounts/login.html'}),
]