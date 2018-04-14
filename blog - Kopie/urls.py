from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.school_list, name='school_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^school/(?P<pk>\d+)/$', views.school_detail, name='school_detail'),
    url(r'^school/new/$', views.school_new, name='school_new'),
    url(r'^school/(?P<pk>\d+)/edit/$', views.school_edit, name='school_edit'),
]
