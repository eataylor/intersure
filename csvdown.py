 
from django.http import HttpResponse
from django.http import HttpRequest

from Isure.models import Attendees
from happenings.models  import Event  

import csv
  

 
# Create your views here.


def csvdown(request):

    this_event = request.GET.get('id')
    event = Event.objects.get(id=this_event)
    print "****** this event ******",this_event

    filename = event.title.replace(' ','')
    #print "****filename="+'"'+filename+'"'

    if event.opentie:
       attendees = Attendees.objects.filter(event=event.opentie.id)
    else:  
       attendees = Attendees.objects.filter(event=int(this_event))
    #attendees = Attendees.objects.filter(event=this_event)
    
    response = HttpResponse(content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    response['Content-Disposition'] = 'attachment; filename="'+filename+'.csv"'
    
    Device = ''
    Meals = ''
    Guestname = ''
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Cell Phone', 'Email','Agency','Title','Device','Reception','Dinner', 'Badge Name', 'Special Needs','Guest Name','Guest Meal1','Guest Meal2','Guest Needs'])
    for item in attendees:
        print "***********dealing with ====>",item.first_name,item.last_name
        if item.devices == "0":
           Device = "Laptop"
        if item.devices == "1":
           Device = "Laptop+Print"
        if item.devices == "2":
           Device = "Print Only"
        if item.meals == True:
           Meals = "Yes"
        else:
           Meals = "No"

        if item.meals2 == True:
           Meals2 = "Yes"
        else:
           Meals2 = "No"

        if item.guestmeals1 == True:
           Guestmeals1 = "Yes"
        else:
           Guestmeals1 = "No"

        if item.guestmeals2 == True:
           Guestmeals2 = "Yes"
        else:
           Guestmeals2 = "No"
        Guestname = item.guest_firstname+' '+item.guest_lastname   
        writer.writerow([item.first_name, item.last_name, item.cellPhone, item.email,item.agencyName,item.attendeeTitle,Device,Meals,Meals2, item.badgename, item.specialneeds,Guestname,
                          Guestmeals1,Guestmeals2,item.guest_specialneeds])

    return response                    
