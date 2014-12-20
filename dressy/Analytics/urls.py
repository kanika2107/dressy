from django.conf.urls import patterns, url
from Analytics import views

urlpatterns = patterns('',
        url(r'^tried/', views.tried, name='tried'),
	url(r'^triedi/',views.triedi, name='triedi'),
	url(r'^followed/',views.followed, name='followed'),
	url(r'^giveUserID/',views.userid),
	url(r'^$',views.home),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
        )
