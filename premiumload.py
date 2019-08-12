from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

from os import listdir

import os
# Create your views here.


def premiumload(request):
    
    print "*******made it to premiumload"

     

    startDir = '/home/tmc/webapps/django110/intersure/PremiumLines/'
     
    Fileslist = os.listdir(startDir)
    for item in Fileslist:
        this_split = item.split("_",2)
        print "***The agency = ",this_split[0],"***The line = ",this_split[1]

    print Fileslist 
     

    return render(request,'premiumload.html', { } )                      
