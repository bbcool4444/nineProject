from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static
from game.views import index, show

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^(?P<game_name>\w+)/show/$', show, name='show'),
)
