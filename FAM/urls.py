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
                       url(r'^list/uncategory_transactions/$',views.uncategory_list,name='uncategory_list'),
                       url(r'^list/total_transaction/$', views.total_transaction, name='total_transaction'),
                       #total_trsactin is main transaction page all option can see ex- add transaction page in ur app
                       #url(r'^category_list/_category/$', views.edit_category,name ='edit_category'),
                       url(r'^total_transaction/edit_amount/$', views.edit_amount,name='edit_amount'),
                       url(r'^total_transaction/vendor/$' ,views.vendor, name= 'vendor'),



)


