
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


def search3(request):
     def buildSearch(post_data):
              search={} 

              if post_data['prin_min']:                  
                 search['principals__gte'] = int(post_data['prin_min'])
                  
              if post_data['prin_max']:                  
                 search['principals__lte'] = int(post_data['prin_max'])
                  

              if post_data['emp_min']:                  
                 search['employees__gte'] = int(post_data['emp_min'])
                  
              if post_data['emp_max']:                  
                 search['employees__lte'] = int(post_data['emp_max'])
                  

              if post_data['rev_min']:                  
                 search['Revenue__gte'] = Decimal(post_data['rev_min'])
                  
              if post_data['rev_max']:                  
                 search['Revenue__lte'] = Decimal(post_data['rev_max'])
                  

              if post_data['comm_min']:                  
                 search['CommPct__gte'] = Decimal(post_data['comm_min'])
                  
              if post_data['comm_max']:                  
                 search['CommPct__lte'] = Decimal(post_data['comm_max'])
                  

              if post_data['bene_min']:                  
                 search['BenePct__gte'] = Decimal(post_data['bene_min'])
                  
              if post_data['bene_max']:                  
                 search['BenePct__lte'] = Decimal(post_data['bene_max'])
                  

              if post_data['pers_min']:                  
                 search['PersPct__gte'] = Decimal(post_data['pers_min'])
                  
              if post_data['pers_max']:                  
                 search['PersPct__lte'] = Decimal(post_data['pers_max'])
                  

              if post_data['ams'] and post_data['ams'] !='choose': 
                 #print "*****AMS = ",ams                 
                 search['AMS__icontains'] = post_data['ams']
                  

              if post_data['crm'] and post_data['crm'] !='choose':
                 #print "*****CRM = ",crm                   
                 search['CRM__icontains'] = post_data['crm']
                  

              if post_data['personals'] and post_data['personals'] !='choose':
                  
                 search['personalvol__Insurer__Name__icontains'] = post_data['personals']
                  
                 if post_data['pervol_min']:
                     
                    search['personalvol__Volume__gte'] = post_data['pervol_min']
                     
                     
                 if post_data['pervol_max']:
                     
                    search['personalvol__Volume__lte'] = post_data['pervol_max'] 
                    
                                        
                  

              if post_data['commercials'] and post_data['commercials'] !='choose':
                 search['commercialvol__Insurer__Name__icontains'] = post_data['commercials']
                  
                 if post_data['commvol_min']:
                     
                    search['commercialvol__Volume__gte'] = post_data['commvol_min']
                     
                 if post_data['commvol_max']:
                     
                    search['commercialvol__Volume__lte'] = post_data['commvol_max']
                                          
                  

              if post_data['employees'] and post_data['employees'] !='choose':
                  
                 search['employeevol__Insurer__Name__icontains'] = post_data['employees']
                  
                 if post_data['emplvol_min']:
                     
                    search['employeevol__Volume__gte'] = post_data['emplvol_min']
                     
                 if post_data['emplvol_max']:
                      
                    search['employeevol__Volume__lte'] = post_data['emplvol_max'] 
                        
              return search
       
         
     if request.user.is_authenticated:
         
                

	print "Enter search "
	active = "search"
        show_result = False
        results = ''
        resultPage =''
        form = SearchForm
        searchfilter = {}
        searchfilter2 = {}
        searchfilterRaw = {}
        if request.POST:
           print "*****>>>In Post *****"
           form = SearchForm(data=request.POST) 
           #print "****form = ",form
           if form.is_valid():
              request.session['PostData'] = request.POST

                                      
               
              searchfilter2 = buildSearch(request.POST)
              #print "****** SearchRaw1 *****",searchfilterRaw1         

              results = Directory.objects.filter(**searchfilter2).order_by('AgencyName')
              #results = Directory.objects.filter(**searchfilter).order_by('AgencyName')
              page = "1"
              paginator = Paginator(results, 5)
              try:
                  resultPage = paginator.page(page)
              except PageNotAnInteger:
                  resultPage = paginator.page(1)
              except EmptyPage:
                  resultPage = paginator.page(paginator.num_pages)
              
              #print "******Starting to set session data *****"
              #print "****** Search filter ******",searchfilter

              request.session['searchfilter'] = ''
              #request.session['searchfilter']= serializers.serialize("json", searchfilter)
              #print "****Num pages ---",paginator.page(paginator.num_pages)
              #print "****length of list =",len(results)
              show_result = True
               
              for item in results:
                  print item.commercialLines.all()
                  print "Agency = {}:  Prin  = {}, emp = {}, Rev  = {}, Comm = {}, Bene = {}, Pers = {},commline = {}".format(item.AgencyName, item.principals,item.employees,item.Revenue,item.CommPct,item.BenePct,item.PersPct,item.commercialvol_set.all() )
                  
           else:
              print "*****Error in Form *****"
	
     
           #return render_to_response('search.html',  RequestContext(request,{'request':request,'form':form,'active':active }))
           print "****** Leaving via render *******"
           return render(request,'search3.html', {'form':form ,'active':active,'results':results,'resultPage':resultPage,'show_result':show_result} )
        else:
           if 'page' in request.GET:
                
               page = request.GET.get('page', 1)
                
               searchfilter = request.session['searchfilter']
               PostData = request.session['PostData']
               

               searchfilter2 = buildSearch(PostData)
               results = Directory.objects.filter(**searchfilter2).order_by('AgencyName')
               #results = Directory.objects.filter(**searchfilter).order_by('AgencyName')
                
               paginator = Paginator(results, 5)
               try:
                  resultPage = paginator.page(page)
               except PageNotAnInteger:
                  resultPage = paginator.page(1)
               except EmptyPage:
                  resultPage = paginator.page(paginator.num_pages)
               
               show_result = True
           else:
               if 'searchfilter' in request.session:
                  del request.session['searchfilter'] 
                  del request.session['PostData'] 

           return render(request,'search3.html', {'form':form ,'active':active,'results':results,'resultPage':resultPage,'show_result':show_result} )

     else:

        print "User is not Authenticated -- Redirecting"
        request.session['nextpage'] = "directory"
        return redirect('login',permanent=True)     
