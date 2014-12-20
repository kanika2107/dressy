from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from home.models import Apparel
from django.http import HttpResponse
from django.template import RequestContext, loader
import os


def login(request):
	    return render(request,'home/login.html')
	    
def home(request):
    context = RequestContext(request)
    apparel_list = Apparel.objects.all()
    context_dict = {'apparel': apparel_list}
    return render_to_response('home/index.html', context_dict, context)


def tried(request):
	if request.user.is_authenticated():
		username = request.user.id
	from allauth.socialaccount.models import SocialToken
	'''stuff = SocialToken.objects.filter(account__user=username, account__provider='facebook')[0]
	from facepy import GraphAPI
	graph=GraphAPI(stuff)
	response = graph.get('me/photos')
	a=[]
	for photo in response['data']:
	     a.append(photo['source'])
	template = loader.get_template('home/display.html')
	context = RequestContext(request, { 'akka': a,
			                 })
        return HttpResponse(template.render(context))'''
    	context = RequestContext(request)
    	social_token = SocialToken.objects.filter(account__user=username, account__provider='facebook')[0]
    	from facepy import GraphAPI
    	graph = GraphAPI(social_token)
    	g = graph.get('me?fields=id,photos.limit(5)')
    	id  = g['id']
    	dic = {}
	a=[]
    	for i in g["photos"]["data"]:
    		dic[i["source"]]=[]
    		for j in i["tags"]["data"]:
    			if(j.has_key('id')):
    				if(j['id']==id):
			             a.append(j['x'])
				     a.append(j['y'])
    			   	     dic[i["source"]].append(j['x'])
    			             dic[i["source"]].append(j['y'])

	template = loader.get_template('home/try.html')
	context = RequestContext(request, {'akka' : dic , "bikka" : a})
	return HttpResponse(template.render(context))

    	





