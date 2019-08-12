
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import Context, Template, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import HttpRequest
from django.core import serializers

from decimal import *

from Isure.forms import SearchForm
from Isure.models  import Directory 


def mutualIndem(request):
     
       
         
     if request.user.is_authenticated:
         
                

	print "Enter Mutual Indem "
	active = "mutual"
        

        return render(request,'mutualIndem.html', {'active':active,} )

     else:

        print "User is not Authenticated -- Redirecting"
        request.session['nextpage'] = "mutual"
        return redirect('login',permanent=True)     
