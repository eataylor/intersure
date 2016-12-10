
"""
This will allow access to Django infrastructure from a python script executed from command line

"""
import csv
import os
import sys
import datetime
from datetime import datetime, date, time
from datetime import *
from django.core.exceptions import ObjectDoesNotExist

sys.path.append('/home/tmc/webapps/django110/intersure/intersure')
os.environ['DJANGO_SETTINGS_MODULE'] = 'intersure.settings'
from  Isure.models import Directory

print "Got here"
d = datetime.strptime('1/01/13', "%m/%d/%y")
now = datetime(2013,1,1)
print now

 
 
ifile  = open('/home/tmc/webapps/django110/intersure/InterSureDirectory.csv', "rb")
reader = csv.DictReader(ifile)
print "***file must  be open ***"
counter=0
 

for row in reader:
  
   if counter > 0:

      
       
  
      member = Directory(AgencyName = row['AgencyName'],BusinessType = row['BusinessType'],PrimaryContactFN = row['PrimaryContactFN'],PrimaryContactLN = row['PrimaryContactLN'],
                ContactTitle = row['ContactTitle'],DirectLine = row['DirectLine'],ContactEmail =  row['Email'],
                HQCountry = row['Country'],HQAddress = row['HQAddress'],HQAddress2 = row['HQAddress2'],HQCity = row['HQCity'],
                HQState = row['HQState'],HQZip = row['HQZip'],Differentiator = row['Differentiator'],KeyContactFN = row['KeyContactFN'],
                KeyContactLN = row['KeyContactLN'],KeyContactEmail= row['KeyContactEmail'],KeyContactPhone = row['KeyContactPhone'])
       
                    
      member.save()
      #print "****Saved item id ",row['id']," at ",str(mem.id)
      
      

       
   counter +=1
print "Counter = ",counter 
ifile.close()
