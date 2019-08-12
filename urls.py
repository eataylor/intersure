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
from intersure.views import eventnews,gallery,partners,partnerstest,IEtest,OOps,disclosures,disclosure990
from intersure.views import SuccessStories2

#from intersure.partners import partners
from intersure.blog import blog
from intersure.blogposts import blogposts
from intersure.directory import directory
from intersure.dirView import dirView
from intersure.dirView1 import dirView1

from intersure.download1 import download1

from intersure.login import login

from intersure.csvdown import csvdown

from intersure.emailEvent import emailEvent

from intersure.enroll import enroll

from intersure.mutualIndem import mutualIndem

from intersure.register import register
from intersure.registeropen1 import registeropen
from intersure.registeropen2 import registeropen2

from intersure.SuccessStory2 import SuccessStory2

from intersure.exit import exit

from intersure.userexit import userexit

from intersure.search import search
from intersure.search2 import search2
from intersure.searchdl import searchdl

from intersure.search3 import search3

from intersure.showregistrants import showregistrants

from intersure.premiumload import premiumload

from intersure.signup import signup

from intersure.testfiles import testfiles

from intersure.videolist import videolist
from intersure.videoshow import videoshow

from photo.imageupload import imageupload

from django.contrib.auth.views import logout

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
    url(r'^about$', about, name='about'),
    url(r'^blog$', blog, name='blog'),
    url(r'^contact$', contact, name='contact'),
    
    url(r'^csvdown$', csvdown, name='csvdown'),

    url(r'^userexit$', userexit, name='userexit'),
    url(r'^disclosures$', disclosures, name='disclosures'),
    url(r'^disclosure990$', disclosure990, name='disclosure990'),
    url(r'^directory$', directory, name='directory'),
    url(r'^dirview$', dirView, name='dirview'),
    url(r'^dirview1$', dirView1, name='dirview1'),

    url(r'^download1$', download1, name='download1'),

    #url(r'^enroll$', enroll, name='enroll'),
    url(r'^register$', register, name='register'),
    url(r'^registeropen$', registeropen, name='registeropen'),
    url(r'^registeropen2$', registeropen2, name='registeropen2'),

    url(r'^emailevent$', emailEvent, name='emailEvent'),

    url(r'^events$', events, name='events'),
    url(r'^eventnews$', eventnews, name='eventnews'),
    url(r'^gallery$', gallery, name='gallery'),

    url(r'^hightest$', hightest, name='hightest'),
    
    url(r'^ietest$', IEtest, name='IEtest'),

    url(r'^imageupload$', imageupload, name='imageupload'),
    url(r'^join$', join, name='join'),
    url(r'^login$', login, name='login'),

    url(r'^exit$', exit, name='exit'),

    url(r'^mutual$', mutualIndem, name='mutual'),

    url(r'^OOps$', OOps, name='OOps'),
    url(r'^partners$', partners, name='partners'),

    url(r'^partnerstest$', partnerstest, name='partnerstest'),

    url(r'^premiumload$', premiumload, name='premiumload'),

    url(r'^imasuccess$', IMASuccess, name='IMASuccess'),
    url(r'^kpdsuccess$', KPDSuccess, name='KPDSuccess'),
    url(r'^rogerssuccess$', RogersSuccess, name='RogersSuccess'),
    url(r'^rossyergersuccess$', RossYergerSuccess, name='RossYergerSuccess'),

    url(r'^search$', search, name='search'),
    url(r'^search2$', search2, name='search2'),
    url(r'^searchdl$', searchdl, name='searchdl'),

    url(r'^search3$', search3, name='search3'),

    url(r'^showregistrants$', showregistrants, name='showregistrants'),

    url(r'^signup$', signup, name='signup'),
    url(r'^successstories$', SuccessStories, name='SuccessStories'),
    url(r'^successstories2$', SuccessStories2, name='SuccessStories2'),
    
    url(r'^successstory2$', SuccessStory2, name='SuccessStory2'),
    
    url(r'^videolist$', videolist, name='videolist'),
    url(r'^videoshow$', videoshow, name='videoshow'),
   


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

admin.site.site_header = 'Intersure Administration'
admin.site.site_title = 'Intersure Site Admin'
admin.site.index_title = 'Manage Intersure Site'

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
