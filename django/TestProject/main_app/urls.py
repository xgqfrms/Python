from django.conf.urls import url
from . import views

urlpatterns = [
    # localhost/index
    url(r'^$', views.index),
]
