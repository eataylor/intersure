from django.shortcuts import redirect
 
 
from django.http import HttpResponse
from django.http import HttpRequest

from django.contrib.auth import logout
from django.contrib import auth 

from intersure.views import index 

 
# Create your views here.


def exit(request):
    
    print "\n\n\n*******made it to logout"
    print "\n\n\n"
    auth.logout(request,next_page="about", template_name='about.html')
    print "\n\n\n***** Should be Logged out now" 
    print "\n\n\n"
    
    return redirect(index,permanent=True)                      
