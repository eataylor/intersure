from django.shortcuts import render,redirect
 
 
from django.http import HttpResponse
from django.http import HttpRequest

from django.contrib.auth import logout
from django.contrib import auth 

from intersure.views import index 

 
# Create your views here.


def userexit(request):
    
    print "\n\n\n*******made it to UserExit"
    print "\n\n\n"
    print "\n\n\n"
    auth.logout(request)
    print "\n\n\n***** Should be Logged out now" 
    print "\n\n\n"
    print "\n\n\n"
    return redirect(index)
    return render(request,'contact.html', {} )                        
