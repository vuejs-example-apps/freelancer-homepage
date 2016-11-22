from django.conf.urls import include, url, patterns
from django.views.generic.base import RedirectView
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings

urlpatterns = [
    url(r'^admin/grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('freelancer_homepage.urls')),
    # url(r'^$', RedirectView.as_view(url='/admin/', permanent=False), name='home')
]

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )
