from django.conf.urls import url

from . import views

app_name = 'aeiot'
urlpatterns = [
    #url(r'^algorithms/$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.AlgorithmsView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<pk>[0-9]+)/algorithm/$', views.AlgorithmUpdate.as_view(), name='algorithm-update'),
    url(r'^new/algorithm/$', views.AlgorithmCreate.as_view(), name='algorithm-create'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]