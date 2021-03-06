__author__ = 'himanshu'
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('osft.views',
    url(r'^create_new_project/$', 'create_new_project'),
    url(r'^project_detail/$', 'project_detail'),
    url(r'^update_project/$', 'update_project'),
)

urlpatterns = format_suffix_patterns(urlpatterns)