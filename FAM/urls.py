from django.conf.urls import patterns, include, url

from django.contrib import admin
from fam_account import views

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'FAM.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^mainpage/$', views.index, name='index'),
                       url(r'^list/$', views.list, name='list'),
                       url(r'^category_list/$', views.category_list, name='category_list'),
                       url(r'^admin/', include(admin.site.urls)),


)


