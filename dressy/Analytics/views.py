from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime  
from .models import ApparelShare
from .models import ApparelTry
from .models import ApparelFollow
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from Analytics.forms import UserForm, UserProfileForm


from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/home/')

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/Analytics/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('Analytics/login.html', {}, context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'Analytics/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def home(request):
    context = RequestContext(request)
    context_dict = {}
    for i in range(1,13):
    	context_dict[str(i)]=len(ApparelShare.objects.filter(apparel_id=i))


    context_dict['Chrome']=len(ApparelShare.objects.filter(browser="Chrome"))
    context_dict['Firefox']=len(ApparelShare.objects.filter(browser="Firefox"))
    context_dict['Safari']=len(ApparelShare.objects.filter(browser="Safari"))
    context_dict['Internet']=len(ApparelShare.objects.filter(browser="Internet Explorer"))
    context_dict['Ubuntu']=len(ApparelShare.objects.filter(os="Ubuntu"))
    context_dict['Windows']=len(ApparelShare.objects.filter(os="Windows"))
    context_dict['MAC']=len(ApparelShare.objects.filter(os="MAC"))
    context_dict['Linux']=len(ApparelShare.objects.filter(os="Linux"))
    context_dict['laptop']=len(ApparelShare.objects.filter(device="laptop"))
    context_dict['mobile']=len(ApparelShare.objects.filter(device="mobile"))
    context_dict['Others']=len(ApparelShare.objects.filter(device="Other"))
    context_dict['Rome']=len(ApparelShare.objects.filter(country="Rome"))
    context_dict['America']=len(ApparelShare.objects.filter(country="America"))
    context_dict['Canada']=len(ApparelShare.objects.filter(country="Canada"))
    context_dict['China']=len(ApparelShare.objects.filter(country="China"))
    context_dict['jftried']=len(ApparelTry.objects.filter(date__month="01"))+len(ApparelTry.objects.filter(date__month="02"))
    context_dict['jffollowed']=len(ApparelFollow.objects.filter(date__month="01"))+len(ApparelFollow.objects.filter(date__month="02"))
    context_dict['jfsharedonf']=len(ApparelShare.objects.filter(date__month="01",shared_on=1))+len(ApparelShare.objects.filter(date__month="02", shared_on=1))
    context_dict['jfsharedong']=len(ApparelShare.objects.filter(date__month="01",shared_on=2))+len(ApparelShare.objects.filter(date__month="02", shared_on=2))
    context_dict['matried']=len(ApparelTry.objects.filter(date__month="03"))+len(ApparelTry.objects.filter(date__month="04"))
    context_dict['mafollowed']=len(ApparelFollow.objects.filter(date__month="03"))+len(ApparelFollow.objects.filter(date__month="04"))
    context_dict['masharedonf']=len(ApparelShare.objects.filter(date__month="03",shared_on=1))+len(ApparelShare.objects.filter(date__month="04", shared_on=1))
    context_dict['masharedong']=len(ApparelShare.objects.filter(date__month="03",shared_on=2))+len(ApparelShare.objects.filter(date__month="04", shared_on=2))
    context_dict['mjtried']=len(ApparelTry.objects.filter(date__month="05"))+len(ApparelTry.objects.filter(date__month="06"))
    context_dict['mjfollowed']=len(ApparelFollow.objects.filter(date__month="05"))+len(ApparelFollow.objects.filter(date__month="06"))
    context_dict['mjsharedonf']=len(ApparelShare.objects.filter(date__month="05",shared_on=1))+len(ApparelShare.objects.filter(date__month="06", shared_on=1))
    context_dict['mjsharedong']=len(ApparelShare.objects.filter(date__month="05",shared_on=2))+len(ApparelShare.objects.filter(date__month="06", shared_on=2))
    context_dict['jatried']=len(ApparelTry.objects.filter(date__month="07"))+len(ApparelTry.objects.filter(date__month="08"))
    context_dict['jafollowed']=len(ApparelFollow.objects.filter(date__month="07"))+len(ApparelFollow.objects.filter(date__month="08"))
    context_dict['jasharedonf']=len(ApparelShare.objects.filter(date__month="07",shared_on=1))+len(ApparelShare.objects.filter(date__month="08", shared_on=1))
    context_dict['jasharedong']=len(ApparelShare.objects.filter(date__month="07",shared_on=2))+len(ApparelShare.objects.filter(date__month="08", shared_on=2))
    context_dict['sotried']=len(ApparelTry.objects.filter(date__month="09"))+len(ApparelTry.objects.filter(date__month="10"))
    context_dict['sofollowed']=len(ApparelFollow.objects.filter(date__month="09"))+len(ApparelFollow.objects.filter(date__month="10"))
    context_dict['sosharedonf']=len(ApparelShare.objects.filter(date__month="09",shared_on=1))+len(ApparelShare.objects.filter(date__month="10", shared_on=1))
    context_dict['sosharedong']=len(ApparelShare.objects.filter(date__month="09",shared_on=2))+len(ApparelShare.objects.filter(date__month="10", shared_on=2))
    context_dict['ndtried']=len(ApparelTry.objects.filter(date__month="11"))+len(ApparelTry.objects.filter(date__month="12"))
    context_dict['ndfollowed']=len(ApparelFollow.objects.filter(date__month="11"))+len(ApparelFollow.objects.filter(date__month="12"))
    context_dict['ndsharedonf']=len(ApparelShare.objects.filter(date__month="11",shared_on=1))+len(ApparelShare.objects.filter(date__month="12", shared_on=1))
    context_dict['ndsharedong']=len(ApparelShare.objects.filter(date__month="11",shared_on=2))+len(ApparelShare.objects.filter(date__month="12", shared_on=2))





    return render_to_response('Analytics/home.html', context_dict, context)

def tried(request):
	merchant_id = request.GET.get('merchant_id', '')
	apparel_id = request.GET.get('apparel_id', '')
	user_id = request.user.id
	date = datetime.now()
#	apparel_id = request.GET.get('apparel_id', '')
#	merchant_id = request.GET.get('merchant_id', '')
#       date = datetime.now()
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
	    IP = x_forwarded_for.split(',')[0]
        else:
	    IP = request.META.get('REMOTE_ADDR')
	device = request.user_agent.device.family
	browser = request.user_agent.browser.family
	os = request.user_agent.os.family
	shared_on=1
#	g = GeoIP()
#	ip = request.META.get('REMOTE_ADDR', None)
#	if ip:
#           city = g.city(ip)['city']
#	else:
	city = 'Rome' # default city
#	data_insert = {
#		          'apparel_id': apparel_id,
#		          'user_id': user_id,
#	                  'merchant_id': merchant_id,
#			  'IP':IP,
#			  'device':device,
#			  'os':os,
#			  'browser':browser,
#			  'date':date,
#			  'country':city,
#			  'shared_on':shared_on,
		                                            
#	}
#        ApparelShare(**data_insert).save()

	c = ApparelShare.objects.create(apparel_id=apparel_id,merchant_id=merchant_id,date=date,IP=IP,country=city,shared_on=shared_on,user_id=user_id,os=os,browser=browser,device=device)[0]
        c.save()
	
	return HttpResponse(user_id)



def triedi(request):
	merchant_id = request.GET.get('merchant_id', '')
	apparel_id = request.GET.get('apparel_id', '')
	user_id = request.user.id
	date = datetime.now()
#	apparel_id = request.GET.get('apparel_id', '')
#	merchant_id = request.GET.get('merchant_id', '')
#       date = datetime.now()
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
	    IP = x_forwarded_for.split(',')[0]
        else:
	    IP = request.META.get('REMOTE_ADDR')
	device = request.user_agent.device.family
	browser = request.user_agent.browser.family
	os = request.user_agent.os.family
	shared_on=2
#	g = GeoIP()
#	ip = request.META.get('REMOTE_ADDR', None)
#	if ip:
#            city = g.city(ip)['city']
#	else:
	city = 'Rome' # default city
	data_insert = {
		          'apparel_id': apparel_id,
		          'user_id': user_id,
	                  'merchant_id': merchant_id,
			  'IP':IP,
			  'device':device,
			  'os':os,
			  'browser':browser,
			  'date':date,
			  'country':city,
			  'shared_on':shared_on,
		                                            
	}
        ApparelShare(**data_insert).save()

#	c = ApparelTry.objects.create(apparel_id=apparel_id,merchant_id=merchant_id,date=date)[0]
#       c.save()
	
	return HttpResponse(user_id)



def followed(request):
	merchant_id = request.GET.get('merchant_id', '')
	apparel_id = request.GET.get('apparel_id', '')
	user_shared_id = request.GET.get('user_id','')
	user_followed_id = request.user.id
	date = datetime.now()
#	apparel_id = request.GET.get('apparel_id', '')
#	merchant_id = request.GET.get('merchant_id', '')
#       date = datetime.now()
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
	    IP = x_forwarded_for.split(',')[0]
        else:
	    IP = request.META.get('REMOTE_ADDR')
	device = request.user_agent.device.family
	browser = request.user_agent.browser.family
	os = request.user_agent.os.family
	shared_on=1
#	g = GeoIP()
#	ip = request.META.get('REMOTE_ADDR', None)
#	if ip:
#           city = g.city(ip)['city']
#	else:
	city = 'Rome' # default city
#	data_insert = {
#		          'apparel_id': apparel_id,
#		          'user_id': user_id,
#	                  'merchant_id': merchant_id,
#			  'IP':IP,
#			  'device':device,
#			  'os':os,
#			  'browser':browser,
#			  'date':date,
#			  'country':city,
#			  'shared_on':shared_on,
		                                            
#	}
#        ApparelShare(**data_insert).save()

	c = ApparelFollow.objects.create(apparel_id=apparel_id,merchant_id=merchant_id,date=date,IP=IP,country=city,shared_on=shared_on,user_id=user_id,os=os,browser=browser,device=device)[0]
        c.save()
	
	return HttpResponse(user_id)

def userid(request):
	return HttpResponse(request.user.id)
