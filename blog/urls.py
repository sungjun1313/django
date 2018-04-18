from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_dat_archive'),
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
    url(r'^search/$', SearchFormView.as_view(), name='search'),
    url(r'^add/$', PostCreateView.as_view(), name='add'),
    url(r'^change/$', PostChangeLV.as_view(), name='change'),
    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name='delete'),
]