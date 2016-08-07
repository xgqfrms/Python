import django.conf.urls
from . import views
# . wildcard character ?

urlpatterns = [
    # localhost/index
    django.conf.urls.url(r'^$', views.index),
]