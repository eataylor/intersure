
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

from decimal import *

from Isure.forms import SearchForm
from Isure.models  import Directory 


def search2(request):
     if request.user.is_authenticated:
         
                

	print "Enter search "
	active = "search"
        show_result = False
        results = ''
        form = SearchForm
        searchfilter = {}
        if request.POST:
           form = SearchForm(data=request.POST) 
           #print "****form = ",form
           if form.is_valid():
             
              prin_min = request.POST['prin_min']
              prin_max = request.POST['prin_max']

              rev_min = request.POST['rev_min']
              rev_max = request.POST['rev_max']

              emp_min = request.POST['emp_min']
              emp_max = request.POST['emp_max']

              comm_min = request.POST['comm_min']
              comm_max = request.POST['comm_max']

              bene_min = request.POST['bene_min']
              bene_max = request.POST['bene_max']

              pers_min = request.POST['pers_min']
              pers_max = request.POST['pers_max']

              crm = request.POST['crm']
              ams = request.POST['ams'] 

              personals = request.POST['personals'] 
              pervol_min = request.POST['pervol_min']
              pervol_max = request.POST['pervol_max']

              commercials = request.POST['commercials'] 
              commvol_min = request.POST['commvol_min']
              commvol_max = request.POST['commvol_max']

              employees = request.POST['employees'] 
              emplvol_min = request.POST['emplvol_min']
              emplvol_max = request.POST['emplvol_max']                        
                        

              
              if prin_min:                  
                 searchfilter['principals__gte'] = int(prin_min)
              if prin_max:                  
                 searchfilter['principals__lte'] = int(prin_max)

              if emp_min:                  
                 searchfilter['employees__gte'] = int(emp_min)
              if emp_max:                  
                 searchfilter['employees__lte'] = int(emp_max)

              if rev_min:                  
                 searchfilter['Revenue__gte'] = Decimal(rev_min)
              if rev_max:                  
                 searchfilter['Revenue__lte'] = Decimal(rev_max)

              if comm_min:                  
                 searchfilter['CommPct__gte'] = Decimal(comm_min)
              if comm_max:                  
                 searchfilter['CommPct__lte'] = Decimal(comm_max)

              if bene_min:                  
                 searchfilter['BenePct__gte'] = Decimal(bene_min)
              if bene_max:                  
                 searchfilter['BenePct__lte'] = Decimal(bene_max)

              if pers_min:                  
                 searchfilter['PersPct__gte'] = Decimal(pers_min)
              if pers_max:                  
                 searchfilter['PersPct__lte'] = Decimal(pers_max)

              if ams and ams !='choose': 
                 print "*****AMS = ",ams                 
                 searchfilter['AMS__icontains'] = ams

              if crm and crm !='choose':
                 print "*****CRM = ",crm                   
                 searchfilter['CRM__icontains'] = crm

              if personals and personals !='choose':
                 print "*****Personals = ",personals
                 searchfilter['personalvol__Insurer__Name__icontains'] = personals
                 if pervol_min:
                    print "*****Pervol_min = ",pervol_min
                    searchfilter['personalvol__Volume__gte'] = pervol_min
                     
                 if pervol_max:
                    print "*****Pervol_max = ",pervol_max
                    searchfilter['personalvol__Volume__lte'] = pervol_man 
                                        
                  

              if commercials and commercials !='choose':
                 print "*****Commercial = ",commercials
                 searchfilter['commercialvol__Insurer__Name__icontains'] = commercials
                 if commvol_min:
                    print "*****commvol_min = ",commvol_min
                    searchfilter['commercialvol__Volume__gte'] = commvol_min 
                 if commvol_max:
                    print "*****commvol_max = ",commvol_max
                    searchfilter['commercialvol__Volume__lte'] = commvol_max                      
                  

              if employees and employees !='choose':
                 print "*****Employees = ",employees
                 searchfilter['employeevol__Insurer__Name__icontains'] = employees
                 if emplvol_min:
                    print "*****emplvol_min = ",emplvol_min
                    searchfilter['employeevol__Volume__gte'] = emplvol_min
                 if emplvol_max:
                    print "*****emplvol_max = ",emplvol_max 
                    searchfilter['employeevol__Volume__lte'] = emplvol_max                    
                  
              
              results = Directory.objects.filter(**searchfilter).order_by('AgencyName')
              print "****length of list =",len(results)
              show_result = True
              for item in results:
                  print "Agency = {}:  Prin  = {}, emp = {}, Rev  = {}, Comm = {}, Bene = {}, Pers = {}".format(item.AgencyName, item.principals,item.employees,item.Revenue,item.CommPct,item.BenePct,item.PersPct)
                  
           else:
              print "*****Error in Form *****"
	
     
        #return render_to_response('search.html',  RequestContext(request,{'request':request,'form':form,'active':active }))
        return render(request,'search2.html', {'form':form ,'active':active,'results':results,'show_result':show_result} ) 

     else:

        print "User is not Authenticated -- Redirecting"
        request.session['nextpage'] = "directory"
        return redirect('login',permanent=True)     
