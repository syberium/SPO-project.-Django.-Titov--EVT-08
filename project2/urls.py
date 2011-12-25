# coding=UTF-8
import os, sys
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('project2.views',
    # Example:
    # (r'^project2/', include('project2.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', 'profile'),
    (r'^$','hello_page'),
    (r'^spo/lecture1/$','lecture_view', {'lecture_name' : 'Лекция 1 СПО','lecture_page':"spolec1.html"}),
    (r'^spo/lecture2/$','lecture_view', {'lecture_name' : 'Лекция 2 СПО','lecture_page':'spolec2.html'}),
    (r'^spo/practice1/$','practice_view', {'practice_name' : 'Практика 1 СПО','practice_page':'spoprac1.html'} ),
    (r'^spo/test/$','test_view',{'test_name': 'Тест по СПО', 'test_id' : 'test_SPO', 'tema': 'СПО'}),
    (r'^ovk/lecture1/$','lecture_view',{'lecture_name' : 'Лекция 1 ОВК','lecture_page':'ovklec1.html'}),
    (r'^ovk/lecture2/$','lecture_view',{'lecture_name' : 'Лекция 2 ОВК','lecture_page':'ovklec2.html'}),
    (r'^ovk/practice1/$','practice_view', {'practice_name' : 'Практика 1 ОВК','practice_page':'ovkprac1.html'}),
    (r'^ovk/test/$','test_view',{'test_name': 'Тест по ОВК', 'test_id' : 'test_OVK', 'tema': 'ОВК'}),
    (r'^ovk/test-complete/$','test_result', {'test_id' :'test_OVK'}),
    (r'^spo/test-complete/$','test_result', {'test_id' :'test_SPO'}),
    (r'^accounts/$', 'red'),
)
