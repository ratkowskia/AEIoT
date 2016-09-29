from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'aeiot'
urlpatterns = [
    #url(r'^algorithms/$', views.IndexView.as_view(), name='index'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.AlgorithmsView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/algorithm/$', views.AlgorithmUpdate.as_view(), name='algorithm-update'),
    url(r'^profile/$', views.ProfileUpdate.as_view(), name='profile-update'),
    url(r'^(?P<pk>[0-9]+)/algorithm/delete/$', views.AlgorithmDelete.as_view(), name='algorithm-delete'),
    url(r'^new/algorithm/$', views.AlgorithmCreate.as_view(), name='algorithm-create'),


]