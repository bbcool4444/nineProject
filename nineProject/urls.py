from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from allGames import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nineProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('game.urls', namespace='game')),
    url(r'^allGames/', include('allGames.urls', namespace='allGames')),
    url(r'^accounts/login', login),
    url(r'^accounts/logout', logout, name='logout'),
    url(r'^accounts/profile', views.profile),
    url(r'^accounts/register', views.register),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
