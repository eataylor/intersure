from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

from django.db import IntegrityError

from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_login
from  django.core.exceptions import ObjectDoesNotExist 

 
from Isure.models  import Videos 

from urlparse import parse_qs
 
# Create your views here.


def videolist(request):
  if request.user.is_authenticated: 
    
    print "*******made it to videolist"
    idlist = []
    videos = Videos.objects.filter( publish = True)
    for item in videos:

        if item.link.find("www.youtube.com") > -1: 
           print "****** YouTube *****"
           qs = item.link.split('?')
           try:
              video_id = parse_qs(qs[1])['v'][0]
              idlist.append(video_id)
              print "****** Video id = ",video_id
           except: 
              idlist.append("***")
        elif item.link.find("www.dropbox.com") > -1:
              print "****** DropBox *****"
              idlist.append("+++")
        else:
              print "****** Something else *****"
              idlist.append("***")
     
    thestuff = zip(videos,idlist) 

    return render(request,'videolist.html', {'videos':videos,'thestuff':thestuff } )

  else:

        print "User is not Authenticated -- Redirecting"
        request.session['nextpage'] = "videolist"
        return redirect('login',permanent=True)                      
