from django.shortcuts import render,redirect
 
 
from django.http import HttpResponse
from django.http import HttpRequest

from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import auth 

from intersure.views import index 
from Isure.forms import OpenEnrollForm,EnrollForm

from Isure.models import Directory,AccessList,Attendees

from happenings.models  import Event 

import geocoder
 
# Create your views here.


def registeropen(request):

     def buildUpdate(request,update_attendee):
         update_attendee.first_name  = request.POST.get('firstname','')
	 update_attendee.last_name =  request.POST.get('lastname','')
	 update_attendee.email  = request.POST.get('youremail','')
	 #print "******Cell Phone back is =====>",request.POST['cellphone']
	 update_attendee.cellPhone  = request.POST.get('cellphone','***')
	 update_attendee.badgename = request.POST.get('badgename','###')
	 #print "****fn = %s, ln= %s, email= %s, cellphone = %s" %(fn,ln,email,cellphone)
	 #print "******Agency name / type = ",request.POST['agencyname'],request.POST['enrolleetype']


	 if "agencyname" in request.POST: 
             
	       update_attendee.agencyName = request.POST['agencyname']

         if "yourtitle" in request.POST: 
	       update_attendee.attendeeTitle = request.POST['yourtitle']
	 

	 if "device" in request.POST:
	     update_attendee.devices  = request.POST['device']
	     print "*****Got Device *****",update_attendee.devices
	 else:
	      
	     print "*****No Device *****"
         if "cellphone" in request.POST:
	     update_attendee.cellphone  = request.POST['cellphone']
	     print "*****Got Celphone *****",update_attendee.devices
	 else:
	     update_attendee.cellphone  = '' 
	     print "*****No Device *****"



	 if "meals" in request.POST:
	      
	     if request.POST['meals'] == "1":
	        update_attendee.meals = True
	     else:
	        if request.POST['meals'] == "0":
	           update_attendee.meals = False 
	        print "*****No meals *****" 
	 else:
	      
	     print "*****No meals *****"

	 if "meals2" in request.POST:
	      
	     if request.POST['meals2'] == "1":
	        update_attendee.meals2 = True
	     else:
	        if request.POST['meals2'] == "0":
	           update_attendee.meals2 = False 
	        print "*****No meals2 *****" 
	 else:
	      
	     print "*****No meals2 *****"

	 if "specialneeds" in request.POST:
	     update_attendee.specialneeds  = request.POST['specialneeds']
	      
	 else:
	      
	     print "*****No specialneeds *****"


	 if "guest_firstname" in request.POST:
	     print "*******GF>>>",request.POST['guest_firstname']
	     update_attendee.guest_firstname  = request.POST['guest_firstname']

	 if "guest_lastname" in request.POST:
	     print "*******GL>>>",request.POST['guest_lastname']
	     update_attendee.guest_lastname  = request.POST['guest_lastname']

	 if "guestspecialneeds" in request.POST:
	     print "*******SN>>>",request.POST['guestspecialneeds']
	     update_attendee.guest_specialneeds  = request.POST['guestspecialneeds']

	 if "guestmeals1" in request.POST:
	      
	     if request.POST['guestmeals1'] == "1":
	        update_attendee.guestmeals1 = True
	     else:
	        if request.POST['guestmeals1'] == "0":
	           update_attendee.guestmeals1 = False 
	        print "*****No guestmeals1 *****" 

	 if "guestmeals2" in request.POST:
	      
	     if request.POST['guestmeals2'] == "1":
	        update_attendee.guestmeals2 = True
	     else:
	        if request.POST['guestmeals2'] == "0":
	           update_attendee.guestmeals2 = False 
	        print "*****No guestmeals2 *****" 
		 


     class Enrollee():
           enrolleetype = '' #1= from Directory, 2= from Access list
           new = ''
           firstname=''
           lastname=''
           agencyname = ''
           badgename = ''
           title = ''
           email=''
           cellphone=''   
     registered = False
     newAttendee = False
     viewtype = 0
     print "\n***********\n****Enter Register Open(1) Event ****\n**************\n"
     
     event=''
     this_loc =''
     form=''
     Geo = ''
     this_enrollee = ''
     if request.user.is_authenticated():
        username = request.user.username
     else:
        username = ''

     
     
     if request.POST: #Posted
        this_viewtype = request.POST['viewtype']
        this_event=request.session["this_eventid"]
        try:
           event = Event.objects.get(id=this_event)
        except: 
           print "Could not Retrieve the Event record for event id {} during Post Request".format(this_event)
           errorlist = []
           errorlist.append("Could not Retrieve the Event record for event id {} during Post Request".format(this_event))
           errorlist.append("The Webmaster has been notified  ")
           request.session['errorlist'] = errorlist
           return redirect('OOps')
         
        loc = event.location.all()
		 
	this_loc = loc[0]
	print "=====>",this_loc.address_line_2+'+'+ this_loc.city +'+'+this_loc.state
	try:
	   Geo = geocoder.google("'"+this_loc.address_line_2+','+ this_loc.city +'+'+this_loc.state + "'")
	except:
	   print "*****Some error from Geo "
	   print "Lat Long == ",Geo.lat,Geo.lng

        if this_viewtype == "0":
           
           form = OpenEnrollForm(data=request.POST)
           if form.is_valid():
              request.session["this_entrantEmail"] = request.POST['youremail']
              this_event=request.session["this_eventid"]
              this_email  = request.POST['youremail']
              try:
                print "**************Trying for attendee"
                attendee = Attendees.objects.get(event=this_event,email=this_email)
                this_enrollee = Enrollee()

                this_enrollee.firstname = attendee.first_name
                this_enrollee.lastname = attendee.last_name
                this_enrollee.cellphone = attendee.cellPhone
		this_enrollee.badgename = attendee.badgename
		this_enrollee.agencyname = attendee.agencyName
		this_enrollee.title = attendee.attendeeTitle

		this_enrollee.email = attendee.email

		this_enrollee.devices = attendee.devices
		this_enrollee.meals = attendee.meals
		this_enrollee.meals2 = attendee.meals2

		this_enrollee.guest_firstname = attendee.guest_firstname
		this_enrollee.guest_lastname = attendee.guest_lastname
		this_enrollee.guest_specialneeds = attendee.guest_specialneeds
		this_enrollee.guestmeals1 = attendee.guestmeals1
		this_enrollee.guestmeals2 = attendee.guestmeals2
		registered = True           


                newAttendee = False
                #this_enrollee = Attendees.objects.get(event=this_event,email=this_email)
                
                print "**************Got attendee"
              except ObjectDoesNotExist:
                print "**************Attendee does not exist"
                #newAttendee = True
                update_attendee = Attendees()
                viewtype = 1
                this_enrollee = Enrollee()
                this_enrollee.email = this_email
	 
	        


              viewtype = 1
           else: #Invalid Email Form
              viewtype = 0
              
              pass

        elif this_viewtype == "1":
             viewtype = 1
             form = EnrollForm(data=request.POST)
             if form.is_valid():
                #this_email  = request.POST['youremail']
                request.session["this_entrantEmail"] = request.POST['youremail']
                this_event=request.session["this_eventid"]
                this_email  = request.POST['youremail']

                try:
		        print "**************Trying for attendee"
		        update_attendee = Attendees.objects.get(event=this_event,email=this_email)
                        buildUpdate(request,update_attendee)
                        update_attendee.save()
		        this_enrollee = Enrollee()

		        this_enrollee.firstname = update_attendee.first_name
		        this_enrollee.lastname = update_attendee.last_name
		        this_enrollee.cellphone = update_attendee.cellPhone
			this_enrollee.badgename = update_attendee.badgename
			this_enrollee.agencyname = update_attendee.agencyName
			this_enrollee.title = update_attendee.attendeeTitle

			this_enrollee.email = update_attendee.email

			this_enrollee.devices = update_attendee.devices
			this_enrollee.meals = update_attendee.meals
			this_enrollee.meals2 = update_attendee.meals2

			this_enrollee.guest_firstname = update_attendee.guest_firstname
			this_enrollee.guest_lastname = update_attendee.guest_lastname
			this_enrollee.guest_specialneeds = update_attendee.guest_specialneeds
			this_enrollee.guestmeals1 = update_attendee.guestmeals1
			this_enrollee.guestmeals2 = update_attendee.guestmeals2
			registered = True           


		        newAttendee = False
		        #this_enrollee = Attendees.objects.get(event=this_event,email=this_email)
		        
		        print "**************Got attendee"
                except ObjectDoesNotExist:
		        print "**************Attendee does not exist"

		        update_attendee = Attendees()
		        buildUpdate(request,update_attendee)
		        update_attendee.event = event 
		        update_attendee.save()
		        this_enrollee = Enrollee()
                        this_enrollee.firstname = update_attendee.first_name
		        this_enrollee.lastname = update_attendee.last_name
		        this_enrollee.cellphone = update_attendee.cellPhone
			this_enrollee.badgename = update_attendee.badgename
			this_enrollee.devices = update_attendee.devices 
			this_enrollee.meals = update_attendee.meals
			this_enrollee.meals2 = update_attendee.meals2
			this_enrollee.guest_firstname = update_attendee.guest_firstname
			this_enrollee.guest_lastname = update_attendee.guest_lastname
			this_enrollee.agencyname = update_attendee.agencyName
			this_enrollee.title = update_attendee.attendeeTitle

			this_enrollee.guestmeals1 = update_attendee.guestmeals1
			this_enrollee.guestmeals2 = update_attendee.guestmeals2

			this_enrollee.guest_specialneeds = update_attendee.guest_specialneeds
			registered = True
                        newAttendee = True
             
               
        return render(request,'registeropen.html', {'form':form,'viewtype':viewtype,'event':event ,'this_loc':this_loc,'this_enrollee':this_enrollee,'registered':registered,'newAttendee':newAttendee,'this_event':this_event,'Geo':Geo} )    





     else: # Not Posted
         print "\n***********NOT POSTED ***********"

         viewtype = 0
         this_event = request.GET.get('id',None)
         if this_event is None:
	      print "**********Didn't get an Event ID from the Get"
              errorlist = []
              errorlist.append("An expected Event Id was not found in url ")
              errorlist.append("The Webmaster has been notified  ")
              request.session['errorlist'] = errorlist
              return redirect('OOps')

         request.session["this_eventid"] = this_event
         try:
            event = Event.objects.get(id=this_event)
            loc = event.location.all()
		 
	    this_loc = loc[0]
	    print "\nLocation =====>",this_loc.address_line_1+'+'+ this_loc.city +'+'+this_loc.state
	    try:
		Geo = geocoder.google("'"+this_loc.address_line_1+','+ this_loc.city +'+'+this_loc.state + "'")
	    except:
		print "*****Some error from Geo "
	    print "Lat Long == ",Geo.lat,Geo.lng  
         except:
            print "Could not Retrieve the Event record for event id {}".format(this_event)
            errorlist = []
            errorlist.append("Could not Retrieve the Event record for event id {}".format(this_event))
            errorlist.append("The Webmaster has been notified  ")
            request.session['errorlist'] = errorlist
            return redirect('OOps')
            

         return render(request,'registeropen.html', {'form':form,'viewtype':viewtype,'event':event ,'this_loc':this_loc,'this_enrollee':this_enrollee,'registered':registered,'this_event':this_event,'Geo':Geo} )
         
