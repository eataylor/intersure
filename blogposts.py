
from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.http import HttpRequest

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

from wordpress_xmlrpc.methods import posts 


def blogposts(request,year,month):

	print "Enter blogposts "
	active = "blog"
        #print "Parms = ",year,month

        request.session['year'] = year
        request.session['month'] = month
        print"*****REDIRECTING *****"
        return redirect("blog")

         
	theseposts = ''
        foundposts = [] 

    	client = Client('http://intersure.tmcmarkets.com/xmlrpc.php', 'taylorea@gmail.com', 'indigo9a')
	theseposts = client.call(posts.GetPosts({'post_status': 'publish'}))
        for item in theseposts:
           print "Item Date Year = ",item.date.year, "Item Date Month = ",item.date.month
           if str(item.date.year) == year and str(item.date.month) == month:
              foundposts.append(item)
        print foundposts
        

	
     
        #return render_to_response('blogposts.html',  RequestContext(request,{'active':active,'foundpostsX':foundposts }))
        return render(request, 'blogposts.html', {'active':active,'foundposts':foundposts })
