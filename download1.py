# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import Context, Template, RequestContext
from django.shortcuts import render,redirect
from django.http import HttpResponse

from decimal import *

from Isure.models import Attendees
from happenings.models  import Event  

#import phonenumbers

import xlsxwriter
# Create your views here.
from django.contrib.auth.decorators import login_required

#@login_required
def download1(request):
    def phone_format(n):
        print "*******n= {}".format(n)
        return format(int(n[:-1]),",").replace(",","-") + n[-1]
    active = ''
    success = False
    
    this_event = request.GET.get('id')
    event = Event.objects.get(id=this_event)
    print "****** this event ******",this_event

    #filename = event.title.replace(' ','')
    filename = '/home/tmc/webapps/django110/intersure/'+event.title.replace(' ','')
    #print "****filename="+'"'+filename+'"'

    if event.opentie:
       attendees = Attendees.objects.filter(event=event.opentie.id)
    else:  
       attendees = Attendees.objects.filter(event=int(this_event))
    #attendees = Attendees.objects.filter(event=this_event)
    
 
    print "**** made it to Download"
     

    guests = 0
    prints = 0
    reception_count = 0 
    dinner_count = 0
    guest_meals1 = 0
    guest_meals2 = 0
        
    
    # Create a new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    topheader_format = workbook.add_format({'bold': True, 'font_size': 16,'align':'center','font_name':'Times New Roman','text_wrap':True,'border': 1,})
    header_format = workbook.add_format({'bold': True, 'font_size': 12,'align':'center','font_name':'Times New Roman','text_wrap':True,'num_format': 'mm/dd/yyyy'})
    cell_format1 = workbook.add_format({'bold': True, 'font_size': 12,'align':'left','font_name':'Times New Roman','num_format': 'mm/dd/yyyy'})
    cell_format2 = workbook.add_format({'bold': False, 'font_size': 12,'align':'left','indent':0,'font_name':'Times New Roman','num_format': 'mm/dd/yyyy'})
    cell_format3 = workbook.add_format({'bold': False, 'font_size': 12,'align':'left','font_name':'Times New Roman','num_format': 'mm/dd/yyyy'})
    cell_format4 = workbook.add_format({'bold': False, 'font_size': 12,'align':'center','font_name':'Times New Roman','num_format': 'mm/dd/yyyy'})

    cell_format5 = workbook.add_format({'bold': False, 'font_size': 12,'align':'center','font_name':'Times New Roman','num_format': '#0'})

    cell_format6 = workbook.add_format({'bold': True,'text_wrap':False, 'font_size': 12,'align':'right','font_name':'Times New Roman','num_format': '#0'})
    
    worksheet.set_column('B:B', 16)   #first name
    worksheet.set_column('C:C', 16)   #last name
    worksheet.set_column('D:D', 12)   #cell Phone
    worksheet.set_column('E:E', 30)    #email
    worksheet.set_column('F:F', 30)   #agency
    worksheet.set_column('G:G', 30)   #title
    worksheet.set_column('H:H', 10)    #device
    worksheet.set_column('I:I', 8)   #reception
    worksheet.set_column('J:J', 8)    #dinner
    
    worksheet.set_column('K:K', 15)    #badge name
    worksheet.set_column('L:L', 15)    #special needs
    worksheet.set_column('M:M', 15)    #Guest name
    worksheet.set_column('N:N', 15)    #Guest Meal1
    worksheet.set_column('O:O', 15)    #Guest Meal2
    worksheet.set_column('P:P', 15)    #Guest Needs
    
    topheader_format.set_pattern(1)
    topheader_format.set_bg_color('gray')
    
    worksheet.merge_range('A1:P2', 'Attendee Information', topheader_format)

    #worksheet.merge_range('I1:P2', 'Tee Shirts', topheader_format)
    
    #worksheet.merge_range('Q1:X2', 'Extra Tee Shirts', topheader_format)

    
    worksheet.write('A3', '',cell_format6)
    worksheet.write('B3', 'First Name',header_format)
    worksheet.write('C3', 'Last Name',header_format)
    worksheet.write('D3', 'Cell Phone',header_format)
    
    worksheet.write('E3', 'Email',header_format)
    worksheet.write('F3', 'Agency',header_format)
    worksheet.write('G3', 'Title',header_format)
    
    worksheet.write('H3', 'Device',header_format)
    worksheet.write('I3', 'Reception',header_format)
    #worksheet.write('I3', 'Tee Shirt size',header_format)

    worksheet.write('J3', 'Dinner',header_format)
    worksheet.write('K3', 'Badge Name',header_format)
    worksheet.write('L3', 'Special Needs',header_format)
    
    worksheet.write('M3', 'Guest Name',header_format)
    worksheet.write('N3', 'Guest Meal1',header_format)
    worksheet.write('O3', 'Guest Meal2',header_format)
    worksheet.write('P3', 'Guest Needs',header_format)
    
     
    #primaries = Attendees.objects.filter(familytie=None,paid=True)
    primaries = []
    row = 3
    for item in attendees:
        guests = guests+1
        worksheet.write(row, 0, ' ',cell_format6)
        worksheet.write(row, 1, item.first_name.capitalize(),cell_format2)
        worksheet.write(row, 2, item.last_name.capitalize(),cell_format2)
        if item.cellPhone.find("-") > 0 or len(item.cellPhone) <= 0:
           worksheet.write(row, 3, item.cellPhone,cell_format2)
        else:
           worksheet.write(row, 3, phone_format(item.cellPhone),cell_format2)
        worksheet.write(row, 4, item.email,cell_format2)
        worksheet.write(row, 5, item.agencyName,cell_format2)
        worksheet.write(row, 6, item.attendeeTitle,cell_format2)
        Device=''
        if item.devices == "0":
           Device = "Laptop"
        if item.devices == "1":
           Device = "Laptop+Print"
           prints = prints+1
        if item.devices == "2":
           Device = "Print Only"
           prints = prints+1
        worksheet.write(row, 7, Device,cell_format2)

        if item.meals == True:
           Meals = "Yes"
           reception_count = reception_count +1
        else:
           Meals = "No"
        worksheet.write(row, 8, Meals,cell_format2)

        if item.meals2 == True:
           Meals2 = "Yes"
           dinner_count = dinner_count +1
        else:
           Meals2 = "No"
        worksheet.write(row, 9, Meals2,cell_format2)

        worksheet.write(row, 10, item.badgename,cell_format2)
        worksheet.write(row, 11, item.specialneeds,cell_format2)

        Guestname = item.guest_firstname+' '+item.guest_lastname
        worksheet.write(row, 12, Guestname,cell_format2)
  
        if item.guestmeals1 == True:
           Guestmeals1 = "Yes"
           guest_meals1 = guest_meals1+1 
        else:
           Guestmeals1 = "No" 
        worksheet.write(row, 13, Guestmeals1,cell_format2)

        if item.guestmeals2 == True:
           Guestmeals2 = "Yes"
           guest_meals2 = guest_meals2+1
        else:
           Guestmeals2 = "No" 
        worksheet.write(row, 14, Guestmeals2,cell_format2)

        worksheet.write(row, 15, item.guest_specialneeds,cell_format2)
     

        

        row = row+1
        


    worksheet.write(row, 0, ' ',cell_format6)
    worksheet.write(row, 1, ' ',cell_format6)
    top = 5
    bottom = row 
    form1 = "=SUM(I{}:I{})".format(top,bottom)
    merge1="E{}:H{}".format(row+2,row+2)
    merge2="A{}:B{}".format(row+2,row+2)
            
    print "Formula is {} ".format(form1)
    print "Merge is {} ".format(merge2)
    cell_format6.set_pattern(1)
    cell_format6.set_bg_color('gray')
    print "***Row is {} format= {} ****".format(row,cell_format6)
    #worksheet.write(merge2, "Guests  =  {}".format(guests),cell_format6)
    worksheet.write(row+1, 0, ' ',cell_format6)
    worksheet.merge_range(merge2, "Guests  =  {}".format(guests),cell_format6)

    merge2="A{}:B{}".format(row+3,row+3)
    worksheet.merge_range(merge2, "Printed Material  =  {}".format(prints),cell_format6)

    merge2="A{}:B{}".format(row+4,row+4)
    worksheet.merge_range(merge2, "Reception Attendence  =  {}".format(reception_count),cell_format6)

    merge2="A{}:B{}".format(row+5,row+5)
    worksheet.merge_range(merge2, "Guest Reception Attendence  =  {}".format(guest_meals1),cell_format6)


    merge2="A{}:B{}".format(row+6,row+6)
    worksheet.merge_range(merge2, "Dinner Attendence  =  {}".format(dinner_count),cell_format6)

    merge2="A{}:B{}".format(row+7,row+7)
    worksheet.merge_range(merge2, "Guest Dinner Attendence  =  {}".format(guest_meals2),cell_format6) 
    
    """
    worksheet.merge_range(merge1, 'Attendee   Totals', topheader_format)               
    worksheet.write_formula(row+1,8, form1,cell_format5,xxl_tot)

    
    form1 = "=SUM(j{}:j{})".format(top,bottom)
    worksheet.write_formula(row+1,9, form1,cell_format5,xl_tot)
    form1 = "=SUM(k{}:k{})".format(top,bottom)
    worksheet.write_formula(row+1,10, form1,cell_format5,l_tot)
    form1 = "=SUM(l{}:l{})".format(top,bottom)
    worksheet.write_formula(row+1,11, form1,cell_format5,m_tot)
    form1 = "=SUM(m{}:m{})".format(top,bottom)
    worksheet.write_formula(row+1,12, form1,cell_format5,s_tot)
    form1 = "=SUM(n{}:n{})".format(top,bottom)
    worksheet.write_formula(row+1,13, form1,cell_format5,kl_tot)
    form1 = "=SUM(o{}:o{})".format(top,bottom)
    worksheet.write_formula(row+1,14, form1,cell_format5,km_tot)
    form1 = "=SUM(p{}:p{})".format(top,bottom)
    worksheet.write_formula(row+1,15, form1,cell_format5,ks_tot)
     

    form1 = "=SUM(q{}:q{})".format(top,bottom)
    worksheet.write_formula(row+1,16, form1,cell_format5,xtra_xxl_tot)
    form1 = "=SUM(r{}:r{})".format(top,bottom)
    worksheet.write_formula(row+1,17, form1,cell_format5,xtra_xl_tot)

    form1 = "=SUM(s{}:s{})".format(top,bottom)
    worksheet.write_formula(row+1,18, form1,cell_format5,xtra_l_tot)
    form1 = "=SUM(t{}:t{})".format(top,bottom)
    worksheet.write_formula(row+1,19, form1,cell_format5,xtra_m_tot)

    form1 = "=SUM(u{}:u{})".format(top,bottom)
    worksheet.write_formula(row+1,20, form1,cell_format5,xtra_s_tot)
    form1 = "=SUM(v{}:v{})".format(top,bottom)
    worksheet.write_formula(row+1,21, form1,cell_format5,xtra_kl_tot)

    form1 = "=SUM(w{}:w{})".format(top,bottom)
    worksheet.write_formula(row+1,22, form1,cell_format5,xtra_km_tot)
    form1 = "=SUM(x{}:x{})".format(top,bottom)
    worksheet.write_formula(row+1,23, form1,cell_format5,xtra_ks_tot)

    form1 = "=SUM(I{}:I{})".format(top,bottom)
    merge1="E{}:H{}".format(row+4,row+4)
      
           
    print "New Formula is {} ".format(form1)
    print "New Merge is {} ".format(merge1)
    worksheet.merge_range(merge1, 'Combined Tee Shirt Totals', topheader_format)
    worksheet.write(row+4,7, "   XXLarge  =  {}".format(xxl_tot+xtra_xxl_tot),cell_format6)    
    worksheet.write(row+5,7, "   XLarge   =  {}".format(xl_tot+xtra_xl_tot),cell_format6)
    worksheet.write(row+6,7, "   Large    =  {}".format(l_tot+xtra_l_tot),cell_format6)
    worksheet.write(row+7,7, "   Medium   =  {}".format(m_tot+xtra_m_tot),cell_format6) 
    worksheet.write(row+8,7, "   Small    =  {}".format(s_tot+xtra_s_tot),cell_format6) 
    worksheet.write(row+9,7, "   Kids Large    =  {}".format(kl_tot+xtra_kl_tot),cell_format6)
    worksheet.write(row+10,7, "   Kids Medium    =  {}".format(km_tot+xtra_km_tot),cell_format6)
    worksheet.write(row+11,7, "   Kids Small    =  {}".format(ks_tot+xtra_ks_tot),cell_format6)                     
    #worksheet.write(row+4,8, xxl_tot+xtra_xxl_tot,cell_format5)
    total_tees = xxl_tot+xtra_xxl_tot+xl_tot+xtra_xl_tot
    total_tees= total_tees + l_tot+xtra_l_tot+m_tot+xtra_m_tot+s_tot+xtra_s_tot+kl_tot+xtra_kl_tot
    total_tees= total_tees + km_tot+xtra_km_tot+ks_tot+xtra_ks_tot
    worksheet.write(row+13,7, "   Total Tees    =  {}".format(total_tees),cell_format6)
    """ 
      
    workbook.close()
    print "***** Workbook is or should be done *****" 
    xldata = open(filename, "rb").read()
    response = HttpResponse(xldata,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
    #return HttpResponse(xldata,content_type='application/pdf')    
    return render(request,'download.html', {'active':active,'success':success,'filename':filename})


