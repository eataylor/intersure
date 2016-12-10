from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

 
# Create your views here.
   
def dirView(request):

    print "***	Enter dirView "
    from Isure.models  import Directory 
    print Directory
    from tagging.registry import register
    from tagging.registry import AlreadyRegistered
    from tagging.models import Tag
    from tagging.utils import calculate_cloud
    from tagging.models import TaggedItem
    
    theseItems =''
    thisname =''
    thisMember =''
    if request.method == 'GET' and 'mem' in request.GET:
       print "****Got get and mem ****"
       mem = request.GET['mem']
       print "*** Mem is = ",mem
       if mem is not None and mem != '':
           
          thisMember = Directory.objects.get(id=int(mem))
          return render_to_response('dirview.html', {'request':request,'thisMember':thisMember }, RequestContext(request)) 
           
           
    else:
       theseItems = Directory.objects.all()
    #return render_to_response('dirview.html', {'theseItems':theseItems,'thisname':thisname }, RequestContext(request))
    return redirect('partners')
