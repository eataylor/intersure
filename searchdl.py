 
from django.http import HttpResponse
from django.http import HttpRequest

from Isure.models import Directory
from happenings.models  import Event 

from decimal import * 

import csv
  

 
# Create your views here.


def searchdl(request):


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


    if 'PostData' not in request.session:

       print "**** Nothing to Download *****"


    else:
       PostData = request.session['PostData']
       searchfilter = buildSearch(PostData)
       results = Directory.objects.filter(**searchfilter).order_by('AgencyName')
       print "****Len of results =====>",len(results) 

     

       filename = "IsuerSearch.csv"
       commLines = ''
       commL = ''
       emplLines = ''
       emplL = ''
       persLines = ''
       persL = '' 

     
    
       response = HttpResponse(content_type='text/csv')
       #response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
       response['Content-Disposition'] = 'attachment; filename="'+filename+'.csv"'
    
     
       writer = csv.writer(response)
       writer.writerow(['Agency Name', 'Principals', 'Employees', 'Revenue','Commercial %',
                     'Benefits %', 'Personal %', 'CRM','AMS','Commercial Lines','Employee Lines','Personal Lines'])
       for item in results:
        commL=''
        emplL = ''
        persL = ''
        commLines = item.commercialvol_set.all()
        for line in commLines:
            if line.Insurer: 
               commL  =  commL+ str(line.Insurer).strip(' ')+"\r\n"

        emplLines = item.employeevol_set.all()
        for line in emplLines:
            if line.Insurer:
               emplL  =  emplL+str(line.Insurer)+"\r\n"

        persLines = item.personalvol_set.all()
        for line in persLines:
            if line.Insurer:
               persL  =  persL+str(line.Insurer)+"\r\n"
             
         
           
        writer.writerow([item.AgencyName, item.principals, item.employees, item.Revenue,item.CommPct,item.BenePct, item.PersPct, item.CRM,item.AMS,commL,emplL,persL])

    return response                    
