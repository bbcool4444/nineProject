from django.conf.urls import patterns, url, include
from django.contrib.auth.views import login, logout
from allGames import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<game_pk>\w+)/show/$', views.show, name='show'),
    url(r'^account/login/$', login, name='login'),
    url(r'^account/logout/$', logout, name='logout'),
)
