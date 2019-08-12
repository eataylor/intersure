from django.shortcuts import render,redirect
 
 
from django.http import HttpResponse
from django.http import HttpRequest

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import auth 

from intersure.views import index 
from Isure.forms import EnrollForm

from Isure.models import Directory,AccessList

from happenings.models  import Event 
 
# Create your views here.


def enroll(request):
     class Enrollee():
           firstname=''
           lastname=''
           email=''   
     
     print "***Enter Enroll ***"
     if request.user.is_authenticated():
	   event=''
	   this_loc=''
	   form=''
           this_enrollee = Enrollee()
           username = request.user.username
           if username == "edward":
              username = "ruthmanka@gmail.com"
           print " ***** BEfore Try with ",username
           try:
              print "****Trying for User",username
              this_user = Directory.objects.get(ContactEmail = username)
              this_enrollee.firstname = this_user.PrimaryContactFN
              this_enrollee.lastname = this_user.PrimaryContactLN 
              this_enrollee.email = this_user.ContactEmail
           except ObjectDoesNotExist:
              try:
                print " ****Trying a second time "
                this_user = AccessList.objects.get(email = username)
                this_enrollee.firstname = this_user.first_name
                this_enrollee.lastname = this_user.last_name
                this_enrollee.email = this_user.email
                
              except ObjectDoesNotExist:
                errorlist = []
                errorlist.append("An error occurred retrieving user database Record using {{%s}} while trying to enroll".format(username))
                errorlist.append("Contact Ruth at xxx-xxx-xxxx")
                request.session['errorlist'] = errorlist
                #request.session['errormsg1'] = "An error occurred retrieving user database Record using {{}} while trying to enroll".format(username)
                #request.session['errormsg2'] = "Call Ruth"
                print "Redirecting --- >",username
                return redirect('OOps')
                  
                
                 

	   if request.POST:
	      form = EnrollForm(data=request.POST)
	       
	   else:
	     this_event = request.GET.get('id')
	     if this_event is None:
		print "Didn't get an Event ID from the Get"
	     else:
		event = Event.objects.get(id=this_event)
		 
		loc = event.location.all()
		 
		this_loc = loc[0]  
		 
	    
	     
	   return render(request,'enroll.html', {'form':form,'event':event ,'this_loc':this_loc,'this_enrollee':this_enrollee} )

     else:
           print "User is not Authenticated -- Redirecting"
           request.session['nextpage'] = "enroll"
           return redirect('login',permanent=True)                       
