from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nineProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('game.urls', namespace='game')),
    url(r'^allGames/', include('allGames.urls', namespace='allGames')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
