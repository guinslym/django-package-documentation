# -*- coding: utf-8 -*
from django.conf.urls import url, include

from . import views
__author__ = 'Guinsly'

app_name = 'tutorial'
urlpatterns = [
      url(r'^home/$', views.IndexView.as_view(), name='index'),
      url(r'^$', views.IndexView.as_view(), name='index'),
]
