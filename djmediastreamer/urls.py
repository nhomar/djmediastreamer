from django.conf.urls import url
from django.contrib.auth.decorators import permission_required

from . import views


urlpatterns = [
    url(r'^$', views.DirectoriesView.as_view(), name='directories'),
    url(r'^mediafiles/(?P<id>[0-9]+)/$',
        views.MediaFilesView.as_view(),
        name='mediafiles'),
    url(r'^watch/(?P<id>[0-9]+)/$',
        views.WatchMediaFileView.as_view(),
        name='watch_mediafile'),
    url(r'^download/(?P<id>[0-9]+)/$',
        views.DownloadMediaFileView.as_view(),
        name='download_mediafile'),
    url(r'^get/(?P<id>[0-9]+)/$',
        views.GethMediaFileView.as_view(),
        name='get_mediafile'),
    url(r'^collect/(?P<id>[0-9]+)/$',
        views.CollectDirectoryView.as_view(),
        name='collect'),
    url(r'^stats/$',
        permission_required('is_staff')(views.StatisticsView.as_view()),
        name='statistics'),
    url(r'^stats/query/$',
        permission_required('is_staff')(views.QueryMediaFilesView.as_view()),
        name='query_mediafiles'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
