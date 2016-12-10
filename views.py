from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

from photo.models  import Album,Image
 
# Create your views here.


def error404(request):


    print "******"+request.META['HTTP_HOST']
    #return render(request,'404.html')
    return render_to_response('404.html', {"request":request}, RequestContext(request))

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

    
    
def index(request):

    print "Enter Index "
    active = "home" 
    from Isure.models  import Directory 
    #print Directory
    from tagging.registry import register
    from tagging.registry import AlreadyRegistered
    from tagging.models import Tag
    print "**** Active = ",active 
     
    return render_to_response('index.html', {'active':active }, RequestContext(request))

def about(request):

    print "Enter about "
    active = "about"
     
     
     
    return render_to_response('about2.html', {'active':active }, RequestContext(request))

def blog(request):

    print "Enter blog "
    active = "blog"
     
     
     
    return render_to_response('blog.html',  RequestContext(request,{'active':active }))


def contact(request):
    from Isure.forms import ContactForm 
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
       
       name = request.POST.get('yourname', '')
               
       email = request.POST.get('youremail', '')
       subj = request.POST.get('yoursubj', '')
       msg = request.POST.get('yourmsg', '') 
       form = ContactForm(data=request.POST) 
                    
       if form.is_valid(): 


          print " ****** Valid Form "
          this_content = Content()
          this_content.name = name
          this_content.subj = subj
          this_content.msg = msg
          this_content.sender = email
          this_content.to.append("ruth@intersure.com")
          mailit(active,this_content)
          print "****Mail should have been sent now ****" 
          msg = "Your Email is on it's way to Intersure"
          
          
       else:
          print " ****** InValid Form "
          print "Errors = ",form.errors
          updatemode = True
          print "**********name = ",name
    else:
       print " ****** Not Posted "
     
     
     
    #return render_to_response('contact.html', {'active':active }, RequestContext(request))
    #return render_to_response('contact.html',  RequestContext(request,{'active':active }))
    return render(request, "contact.html", {'form':form,'active':active,'name':name,'email':email,'subj':subj,'msg':msg,'updatemode':updatemode})


def eventnews(request):

    print "Enter eventnews "
    active = "eventnews"
     
     
     
    return render_to_response('eventNews.html', {'active':active }, RequestContext(request))
    #return render_to_response('eventNews.html', {'active':active }, RequestContext(request))




def events(request):

    print "Enter events "
    active = "events"
     
     
     
    return render_to_response('events.html', {'active':active }, RequestContext(request))



def gallery(request):

    print "Enter gallery "
    active = "gallery"
   
    albums = Album.objects.all()
    for album in albums:
      thelist = album.images_as_list()
      for item in thelist:
          print "************",item 
       
       
     
     
     
    return render_to_response('gallery.html', {'active':active }, RequestContext(request))

def hightest(request):

    print "Enter hightest "
    active = "gallery"
   
     
       
       
     
     
     
    return render_to_response('hightest.html', {'active':active }, RequestContext(request))



    
def IMASuccess(request):

    print "Enter IMA Success "
     
     
     
    return render_to_response('IMASuccess.html', { }, RequestContext(request))

def join(request):

    print "Enter join "
    active = "join"
    from Isure.forms import ContactForm 
    from intersure.mailit import mailit
     
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
       
       name = request.POST.get('yourname', '')
               
       email = request.POST.get('youremail', '')
       subj = request.POST.get('yoursubj', '')
       msg = request.POST.get('yourmsg', '') 
       form = ContactForm(data=request.POST) 
                    
       if form.is_valid(): 


          print " ****** Valid Form "
          this_content = Content()
          this_content.name = name
          this_content.subj = subj
          this_content.msg = msg
          this_content.sender = email
          this_content.to.append("ruth@intersure.com")
          mailit(active,this_content)
          print "****Mail should have been sent now ****" 
          msg = "Your Email is on it's way to Intersure"
          
          
       else:
          print " ****** InValid Form "
          print "Errors = ",form.errors
          updatemode = True
          print "**********name = ",name
    else:
       print " ****** Not Posted "
     
     
     
     
    return render(request, "join1.html", {'form':form,'active':active,'name':name,'email':email,'subj':subj,'msg':msg,'updatemode':updatemode})

     
     
     
    #return render_to_response('join1.html', {'active':active }, RequestContext(request))

        
def KPDSuccess(request):

    print "Enter KPD Success "
     
     
     
    return render_to_response('KPDSuccess.html', { }, RequestContext(request))

def partners(request):
    from geopy.geocoders import Nominatim
    import geocoder
    from Isure.models  import Directory 

    print "Enter Partners "
    active = "partners"
    thisplace = ''
    class loc:
      lat = ''
      lng = '' 
    latlongs = []
    #geolocator = Nominatim()
    members = Directory.objects.all()
    print " ***** the number of Members is ",len(members)
    for item in members:
       print "*****Item = ",item.AgencyName,item.HQAddress,item.HQCity  
       #thisplace = item.HQAddress+' '+ item.HQCity 
       #print "***** this place = ",thisplace 
       #location = geolocator.geocode(thisplace)
       g = geocoder.google(item.HQAddress+' '+ item.HQCity)
       if g.lat != None:
          item.HQLat= g.lat
          item.HQLong= g.lng
          item.save()
          thisloc = loc()
          thisloc.lat = g.lat
          thisloc.lng = g.lng
          latlongs.append(thisloc)
          print "address = ",item.AgencyName.encode('utf-8'),item.HQAddress+' '+ item.HQCity, "geocode = ",g.lat,g.lng
        
        
     
     
    for item in latlongs:
       print item.lat,item.lng 
    return render_to_response('partners2.html', {'active':active }, RequestContext(request))


def partnerstest(request):
    from geopy.geocoders import Nominatim
    import geocoder
    from Isure.models  import Directory 

    print "Enter Partners test "
    active = "partners"
    thisplace = ''
    class loc:
      lat = ''
      lng = '' 
    latlongs = []
    #geolocator = Nominatim()
    members = Directory.objects.all()
    print " ***** the number of Members is ",len(members)
    for item in members:
       print "*****Item = ",item.AgencyName,item.HQAddress,item.HQCity  
       #thisplace = item.HQAddress+' '+ item.HQCity 
       #print "***** this place = ",thisplace 
       #location = geolocator.geocode(thisplace)
       g = geocoder.google(item.HQAddress+' '+ item.HQCity)
       if g.lat != None:
          item.HQLat= g.lat
          item.HQLong= g.lng
          item.save()
          thisloc = loc()
          thisloc.lat = g.lat
          thisloc.lng = g.lng
          latlongs.append(thisloc)
          print "address = ",item.AgencyName.encode('utf-8'),item.HQAddress+' '+ item.HQCity, "geocode = ",g.lat,g.lng
        
        
     
     
    for item in latlongs:
       print item.lat,item.lng 
    return render_to_response('partners2a.html', {'active':active }, RequestContext(request))



def SuccessStories(request):

    print "Enter Success Stories "
     
     
     
    return render_to_response('SuccessStories1.html', { }, RequestContext(request))



def RogersSuccess(request):

    print "Enter Rogers Success "
     
     
     
    return render_to_response('RogersSuccess.html', { }, RequestContext(request))

def RossYergerSuccess(request):

    print "Enter Ross Yerger Success "
     
     
     
    return render_to_response('RossYergerSuccess.html', { }, RequestContext(request))
            

