from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

from Isure.models  import HotTopic
 

import os
# Create your views here.


def testfiles(request):
    
    print "*******made it to testfiles"

    """

    wp = Client('http://intersure.com/xmlrpc.php', 'taylorea@gmail.com', 'indigo9a')
    wp.call(GetPosts())

    startDir = '/home/tmc/webapps/testintersure/wp-content/uploads/'
    for dirName, subdirList, fileList in os.walk(startDir):
        if (dirName.find("/2013/") > -1  or  dirName.find("/2014/") > -1 or
           dirName.find("/2015/") > -1 or dirName.find("/2016/")  > -1 ):
           for item in fileList:
             if item.find(".pdf") > 0:
                print " \n****Found Arcive file '%s'  \n%s "  % (dirName,item)
     
     
    """
    #return render(request,'testfiles.html', { } )
    thistopic = ''

    hottopic = HotTopic.objects.filter(publish = True).order_by('-postDate')[:1]
    if len(hottopic) > 0:
       thistopic = hottopic[0]
    if thistopic:
       print "****Found "
    else:
       print "*****Not found "  

    return render(request,'indextest.html', {'thistopic':thistopic } ) 


def testmain(request):   





    return render(request,'testfiles.html', { } )                   
