# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import kidvietnamese
urlpatterns = patterns('kidvietnamese.views',
  url(r'^index/$','index'),#這樣做似乎是對應到首頁
)