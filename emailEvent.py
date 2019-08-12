from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest


 
# Create your views here.



def emailEvent(request):
    from Isure.forms import EmailEventForm
    from intersure.mailit import mailit
    print "Enter contact "
    active = "contact"
    form = ''
    name = ''
    email = ''
    subj = ''
    msg = ''
    updatemode = False
    class Content:
          name = ''
          subj = ''
          msg  = ''
          sender = ''
          to = []
    if request.POST:
       print "***Posted = ",request.POST
       
        
       subj = request.POST.get('subj', '')
       message = request.POST.get('message', '') 
       form = EmailEventForm(data=request.POST) 
                    
       if form.is_valid(): 


          print " ****** Valid Form "
          this_content = Content()
          this_content.name = name
          this_content.subj = subj
          this_content.msg = msg
          this_content.sender = email
          this_content.to.append("ruth@intersure.com")
          #mailit(active,this_content)
          print "****Mail should have been sent now ****" 
          msg = "Your Email is on its way to Intersure"
          
          
       else:
          print " ****** InValid Form "
          print "Errors = ",form.errors
          updatemode = True
          print "**********name = ",name
    else:
       print " ****** Not Posted "
     
     
     
     
    return render(request, "emailEvent.html", {'form':form,'active':active,'name':name,'email':email,'subj':subj,'msg':msg,'updatemode':updatemode})


