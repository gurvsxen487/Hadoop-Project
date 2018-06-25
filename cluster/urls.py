from django.conf.urls import url , include
from . import views
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


app_name = 'cluster'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^postsignup/$', views.postsignup, name='postsignup'),
    url(r'^postsignin/$', views.postsignin, name='postsignin'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^service_status/$', views.service_status, name='service_status'),
    url(r'^about/$', views.about, name='about'),
    url(r'^settings/$', views.settings, name='settings'),
    
    # Dashboard
    url(r'^clear_cluster/$', views.clear_cluster, name='clear_cluster'),

]
