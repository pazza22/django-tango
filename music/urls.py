from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/232/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/232/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
