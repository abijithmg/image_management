from django.conf.urls import url, include
from rest_framework.authtoken import views as auth_token_views
# from rest_framework import routers

from api import views


urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^api-token-auth/', auth_token_views.obtain_auth_token),
    url(r'^img_upload/$', views.img_upload, name='img_upload'),
    url(r'^img_list/$', views.img_list, name='img_list'),
    url(r'^img_detail/$', views.img_detail, name='img_detail'),
]
