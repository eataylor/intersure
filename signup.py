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

from Isure.forms import SignupForm
from Isure.models  import Directory, AccessList 
 
# Create your views here.


def signup(request):
    
    print "*******made it to Signup"
     
    form=''
    username = ''
    password = ''
    msg = ''
    ln = ''
    fn = ''
    buildUser = False
    
    if request.POST:
       form = SignupForm(data=request.POST)
        
        
                    
       if form.is_valid():

         formemail = request.POST['email_id']
         password = request.POST['password']
         try:
            thisMember = Directory.objects.get(ContactEmail=formemail)
            fn = thisMember.PrimaryContactFN
            ln = thisMember.PrimaryContactLN
            buildUser = True 
         except ObjectDoesNotExist:
            try:
               thisAccess = AccessList.objects.get(email=formemail)
               fn = thisAccess.first_name
               ln = thisAccess.last_name
               buildUser = True
            except ObjectDoesNotExist:
               print "**** Email not in either directory "
               msg = "There is some Problem with your email address %s - Call Ruth "%(formemail)

         if buildUser: 
		 thisUser = User()
		 thisUser.username = formemail
		 thisUser.email = formemail
		 thisUser.first_name = fn
		 thisUser.last_name = ln
		 thisUser.set_password(password) 
		 thisUser.is_active = True
		 #print "*****After checking password = ",thisUser.check_password(password)
		 try:
		    thisUser.save()
		    print "User Saved"
                    return redirect("directory")
		 except IntegrityError as e:
		    print "Intergrity error cause = ",e.__cause__ 
		    if str(e.__cause__).find('Duplicate entry') > -1:
		       print "**** Found the  cause "
		       msg = "There is already a user with %s as a Username "%(formemail)
		    else:
		       print "**** Did not find the cause" 
		       msg = "An unknown Database error has occurred. Your webmaster has been notified " 

       else:
          print "Invalid Form",form.errors
       #   username = request.POST['username']
       #  password = request.POST['password']
             
     
     

    return render(request,'signup.html', {'msg':msg,'form':form ,'username':username,'password':password} )                      
