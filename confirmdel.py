from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest


from django.contrib.auth.models import User
 
from  django.core.exceptions import ObjectDoesNotExist 

 
from Isure.models  import Directory, AccessList 
 
# Create your views here.


def confirmdel(request):
    
    print "*******made it to confirmdel"
     
    sessionerror =''
     
    
    if request.POST: # Posted
       print " ******* Do the Deletes *****"
       return redirect("/showregistrants?id=12")   
        
        
                    
    else: # Not Posted
        del_list = request.session.get('del_list', '')
        event = request.session.get('event', '')
   
        if del_list and event:
           print "****** Got the delete list *****"
           request.session['this_list'] = request.session['del_list']
           request.session['this_event'] = request.session['event']
           del request.session['del_list']
           del request.session['event']
        else:
           print "*****Did not get both event and delete list ****** event =",event,", del_list = ",del_list
           msg = "*****Did not get both event and delete list ****** event ="+str(event)+", del_list = "+str(del_list)
           sessionerror = True
        
             
     
     

    return render(request,'ConfirmDel.html', {'sessionerror':sessionerror,'msg':msg } )  

                    
