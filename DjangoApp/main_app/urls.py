import django.conf.urls
from . import views

urlpatterns = [
    # localhost/index
    django.conf.urls.url(r'^$', views.index),
]