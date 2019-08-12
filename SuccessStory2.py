from django.shortcuts import render 
 
 
from django.http import HttpResponse
from django.http import HttpRequest

from Isure.models  import SuccessStory  

from intersure.views import index 

 
# Create your views here.


def SuccessStory2(request):
    story = ''
    stories = ''
    view_type = ''
    
    if request.method == 'GET' and 'story' in request.GET:
       story_id = request.GET['story']
       story = SuccessStory.objects.get(id= int(story_id))
       
       view_type = '1'
    else: 

       stories = SuccessStory.objects.filter(publish = True)
       view_type = '2' 
    
     
    return render(request,'SuccessStory2.html', {'stories':stories,'story':story,'view_type':view_type} )                        
