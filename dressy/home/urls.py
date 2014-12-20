from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^try/', views.tried, name='tried'),
	url(r'^login/',views.login, name='login'),
        )
