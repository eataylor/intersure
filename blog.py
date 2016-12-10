
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

from wordpress_xmlrpc.methods import posts 


def blog(request):

	print "Enter Blog "
	active = "blog"
        thisyear = ''
        thismonth = ''
        year = ''
        month = ''
        textmonth = ''
        months = ['January','February','March','April','May','June','July','August','September','October','November','December'] 
        #del request.session['month']
        #del request.session['year']
        if 'year' in request.session:
           thisyear = request.session['year']
           del request.session['year'] 
        if 'month' in request.session:
           thismonth = request.session['month']
           textmonth = months[int(thismonth)-1]
           del request.session['month'] 

        print "This year = ",thisyear,"this month = ",thismonth

         
	theseposts = ''

    	client = Client('http://intersure.tmcmarkets.com/xmlrpc.php', 'taylorea@gmail.com', 'indigo9a')


	theseposts = client.call(posts.GetPosts({'post_status': 'publish'}))

        if thisyear and thismonth:
           print "****Doing thisyear thismonth "
           foundposts = []
           for item in theseposts:
              print "Item Year = ",item.date.year, "Item  Month = ",item.date.month
              if str(item.date.year) == thisyear and str(item.date.month) == thismonth:
                 print "*****Appending *****"
                 foundposts.append(item)
              else:
                 print "***** NOT APPENDED *****",item.date.year,item.date.month
           theseposts = foundposts

	
     
        return render_to_response('blog.html',  RequestContext(request,{'active':active,'theseposts':theseposts,'textmonth':textmonth,'thisyear':thisyear }))
