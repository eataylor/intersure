"""intersure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
print "\n\nEnter urls \n\n"
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import  include

from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

from intersure.views import about,events,index,contact,join,IMASuccess,KPDSuccess,RogersSuccess,RossYergerSuccess,SuccessStories,hightest
from intersure.views import eventnews,gallery,partners,partnerstest

#from intersure.partners import partners
from intersure.blog import blog
from intersure.blogposts import blogposts
from intersure.directory import directory
from intersure.dirView import dirView
from intersure.login import login
from intersure.exit import exit

from intersure.userexit import userexit

from intersure.search import search

from intersure.signup import signup

from intersure.testfiles import testfiles

from photo.imageupload import imageupload

from django.contrib.auth.views import logout

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
    url(r'^about$', about, name='about'),
    url(r'^blog$', blog, name='blog'),
    url(r'^contact$', contact, name='contact'),
    url(r'^userexit$', userexit, name='userexit'),
    url(r'^directory$', directory, name='directory'),
    url(r'^dirview$', dirView, name='dirview'),
    url(r'^events$', events, name='events'),
    url(r'^eventnews$', eventnews, name='eventnews'),
    url(r'^gallery$', gallery, name='gallery'),

    url(r'^hightest$', hightest, name='hightest'),

    url(r'^imageupload$', imageupload, name='imageupload'),
    url(r'^join$', join, name='join'),
    url(r'^login$', login, name='login'),
    url(r'^exit$', exit, name='exit'),
    url(r'^partners$', partners, name='partners'),

    url(r'^partnerstest$', partnerstest, name='partnerstest'),

    url(r'^imasuccess$', IMASuccess, name='IMASuccess'),
    url(r'^kpdsuccess$', KPDSuccess, name='KPDSuccess'),
    url(r'^rogerssuccess$', RogersSuccess, name='RogersSuccess'),
    url(r'^rossyergersuccess$', RossYergerSuccess, name='RossYergerSuccess'),

    url(r'^search$', search, name='search'),
    url(r'^signup$', signup, name='signup'),
    url(r'^successstories$', SuccessStories, name='SuccessStories'),
    url(r'^testfiles$', testfiles, name='testfiles'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', blogposts, name='blogposts'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1})/$', blogposts, name='blogposts'),

    url(r'^logout/$', logout, {'next_page': '/login'}),


    url(r'^calendar/', include('happenings.urls', namespace='calendar')),

    #url(r'^photologue/', include('photologue.urls', namespace='photologue')),


    url(r'^admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^photos/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/tmc/webapps/django110/intersure/photos/'}),


] 

if settings.DEBUG:
    print "Settings is Debug "
    urlpatterns += [
        url(r'^photos/(?P<path>.*)$', serve, {
            'document_root': '/home/tmc/webapps/django110/intersure/Isure/static/photos/',
        }),
        url(r'^images/(?P<path>.*)$', serve, {
            'document_root': '/home/tmc/webapps/django110/intersure/Isure/static/lightbox_slideshow/images/',
        }),

    ]
