from django.conf.urls import patterns, url, include
from allGames import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<game_pk>\w+)/show/$', views.show, name='show'),
    url(r'^comments/$', views.comments, name='comments'),
    url(r'^comments/post/$', views.post, name='post'),
)
