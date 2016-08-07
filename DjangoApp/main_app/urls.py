#!/usr/bin/python
#  -*- coding: utf-8 -*-
import django.conf.urls
from . import views
# . wildcard character(通配符) ?

urlpatterns = [
    # localhost/index
    django.conf.urls.url(r'^$', views.index),
]