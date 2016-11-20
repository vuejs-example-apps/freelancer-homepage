from django.conf.urls import include, url, patterns
from .views import api_snapshot

urlpatterns = (
    url(r'^api/snapshot.json$', api_snapshot, name='api.snapshot'),
)
