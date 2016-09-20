from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^aeiot/', include('aeiot.urls')),
    url(r'^$', include('aeiot.urls')),
    url(r'^admin/', admin.site.urls),
]