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

import datetime

 
from Isure.models  import Directory, AccessList
from Isure.models  import Videos,VideoViewers 

from urlparse import parse_qs 
 
# Create your views here.


def videoshow(request):
  if request.user.is_authenticated:     
    print "*******made it to videoshow"
    this_user = request.user
    print "****** this user is -",this_user
    this_video = ''
    this_type = ''
    this_id = request.GET.get('id', '') 
    print "*****this Video Id = ",this_id
    if this_id:
       this_video = Videos.objects.get( id=int(this_id) )
       print "**** This Video link = ",this_video.link
       if this_video.link.find("www.youtube.com") > -1: 
          qs = this_video.link.split('?')
          #qs = this_video.link
          video_id = parse_qs(qs[1])['v'][0]
          this_type = 'y'
        
          print "****** Video id = ",video_id
       elif this_video.link.find("www.dropbox.com") > -1:
          print "****** DropBox *****"
          video_id = this_video.link.replace("www.dropbox.com","dl.dropboxusercontent.com")
          this_type = 'd'
       else:
          video_id = "***" 
         
       
    else:
       video_id = "***"  
    
     
    if video_id != "***":
       viewer_info = User.objects.get(username = this_user)
       try:
          videoviewer = VideoViewers.objects.get(video = this_video,viewer = viewer_info.email)
          videoviewer.view_cnt += 1
          videoviewer.save()
       except ObjectDoesNotExist:
          videoviewer = VideoViewers()
          videoviewer.video = this_video
          videoviewer.viewer = viewer_info.email
          videoviewer.view_cnt = 1
          videoviewer.viewDate = datetime.datetime.now().date()
          videoviewer.save() 
       print "*****viewer info = ",viewer_info.email
    
    return render(request,'videoshow.html', {'this_video':this_video,'video_id':video_id,'this_type':this_type } )   

  else:

        print "User is not Authenticated -- Redirecting"
        request.session['nextpage'] = "videolist"
        return redirect('login',permanent=True)                      
