from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
 
# Create your views here.




    
@login_required    
def partners(request):

    print "Enter Partner "
    active = "partners"
    from Isure.models  import Directory 
    print Directory
    from tagging.registry import register
    from tagging.registry import AlreadyRegistered
    from tagging.models import Tag
    from tagging.utils import calculate_cloud
    from tagging.models import TaggedItem

     
     
    theseItems=''
    thisname=''
    if request.method == 'GET' and 'spec' in request.GET:
       print "****Got get and spec ****"
       spec = request.GET['spec']
       print "*** Spec is = ",spec
       if spec is not None and spec != '':
           
          spec_tag = Tag.objects.get(id=int(spec))
          thisname = spec_tag.name
          theseItems = TaggedItem.objects.get_by_model(Directory, spec_tag)
          print "these items = ",theseItems, len(theseItems)
    else:
       theseItems = Directory.objects.all()
    return render_to_response('partner.html', {'theseItems':theseItems,'thisname':thisname,'active':active }, RequestContext(request))
