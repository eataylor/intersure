from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_login

from Isure.forms import AuthenticationForm
from Isure.models import Attendees
from happenings.models  import Event

 
# Create your views here.


def showregistrants(request):
    
    print "*******made it to show Registrants"
     
    form=''
    username = ''
    password = ''
    attendees = ''
    event = ''
    del_list = []
    
    if request.POST:

       print "****** Enter Post leg of if "
       this_event = request.GET.get('id')
       print "******This Event = ",this_event
       event = Event.objects.get(id=this_event)
       print "**********Open Tie = ",event.opentie
       if event.opentie:
          attendees = Attendees.objects.filter(event=event.opentie.id)
       else:  
          attendees = Attendees.objects.filter(event=int(this_event))
       print "***Count of attendees ****= ",len(attendees)
       updates={} 
       for item in attendees:

            

            

           if request.POST.has_key('badgename-'+str(item.id)):
                 print "*****Badgenanme = ",request.POST['badgename-'+str(item.id)]                  
                 item.badgename = request.POST['badgename-'+str(item.id)]
           else:
              print "*****Badgename = ",request.POST['badgename-'+str(item.id)]

           if request.POST.has_key('guestname-'+str(item.id)):
                 print "*****Guestnanme = ",request.POST['guestname-'+str(item.id)]                  
                 namesplit = (request.POST['guestname-'+str(item.id)].split(' '))
                 print "*****Len of namesplit ",len(namesplit)
                 item.guest_firstname = namesplit[0] 
                 if len(namesplit) >1:
                   item.guest_lastname = namesplit[1]
           if request.POST.has_key('meals-'+str(item.id)):
              if request.POST['meals-'+str(item.id)] == "1":
                 item.meals = True 
              if request.POST['meals-'+str(item.id)] == "0":
                 item.meals = False

           if request.POST.has_key('guestmeals1-'+str(item.id)):
              if request.POST['guestmeals1-'+str(item.id)] == "1":
                 item.guestmeals1 = True 
              if request.POST['guestmeals1-'+str(item.id)] == "0":
                 item.guestmeals1 = False 

           if request.POST.has_key('guestmeals2-'+str(item.id)):
              if request.POST['guestmeals2-'+str(item.id)] == "1":
                 item.guestmeals2 = True 
              if request.POST['guestmeals2-'+str(item.id)] == "0":
                 item.guestmeals2 = False 

           if request.POST.has_key('devices-'+str(item.id)): 
                 item.devices =  request.POST['devices-'+str(item.id)]
           else:
                 print "****** Device key not found "
 
           item.save()

       if del_list:
          print "\n\nThere are items to delele",len(del_list)
       else:
          print "\n\nNothing to delete " 
       #attendees = Attendees.objects.filter(event=this_event)
       if event.opentie:
          attendees = Attendees.objects.filter(event=event.opentie.id)
       else:  
          attendees = Attendees.objects.filter(event=int(this_event)) 
           

    else:

      this_event = request.GET.get('id')
      try:
         event = Event.objects.get(id=this_event)
         print "****** this Event ******",this_event
         
      except Event.DoesNotExist:
         
         print "*******Dd not find the Event *******"

       
      if event.opentie:
           print "**********Open Tie = ",event.opentie.id
           attendees = Attendees.objects.filter(event=event.opentie.id)
      else:
           print "**********NONE Open Tie side = "  
           attendees = Attendees.objects.filter(event=int(this_event))
      #attendees = Attendees.objects.filter(event=this_event)
       
    return render(request,'showregistrants.html', {'form':form,'attendees':attendees,'event':event } )                      
