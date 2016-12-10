from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_login

from Isure.forms import AuthenticationForm

 
# Create your views here.


def login(request):
    
    print "*******made it to login"
     
    form=''
    username = ''
    password = ''
    
    if request.POST:
       form = AuthenticationForm(data=request.POST)
       #print "*****"
        
       #print form
        
       #logout(request)
        
                    
       if form.is_valid():

          print "**********Valid Form"
          user = request.POST['username']
          passw = request.POST['password']
           
          u = authenticate(username=user, password=passw)
          if u is not None:
             if u.is_active:
                auth_login(request, u)
                print "****Should be logged in now ****"
                #return redirect('am.html', foo='bar')
                 
                #frompaypal = request.session['frompaypal']
                
                 
                if 'nextpage' in request.session:
                    print "****Found Nextpage in Login " 
                    nextpage = request.session['nextpage']
                    del request.session['nextpage'] 
                    return redirect('/'+nextpage,permanent=True)

                
             else:
                 print "***User not Active***"   
          else:
             print ("***NOT Authenticated****")

       else:
          print "Invalid Form"
          username = request.POST['username']
          password = request.POST['password']
          #print "form username = ",form.id_Username   
     
    #return render_to_response('login.html', {'form':form ,'username':username,'password':password},RequestContext(request))

    return render(request,'login.html', {'form':form ,'username':username,'password':password} )                      
