from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ApparelTry(models.Model):
	apparel_id = models.IntegerField()
	merchant_id = models.IntegerField()
	device = models.CharField(max_length=1000)
        #0 for laptop 1 for mobile 2 for tablet
	os = models.CharField(max_length=1000)
	browser = models.CharField(max_length=1000)
	date = models.DateTimeField()
	IP = models.IPAddressField()
	country = models.CharField(max_length=1000)
	user_id = models.IntegerField()

	def __unicode__(self):
		return str(self.apparel_id)

class ApparelShare(models.Model):
	       apparel_id = models.IntegerField()
	       merchant_id = models.IntegerField()
	       device = models.CharField(max_length=1000)
	       #0 for laptop 1 for mobile 2 for tablet
               os = models.CharField(max_length=1000)
	       browser = models.CharField(max_length=1000)
	       date = models.DateTimeField()
               IP = models.IPAddressField()
               country = models.CharField(max_length=1000)
               user_id = models.IntegerField()
	       shared_on = models.IntegerField()
	       def __unicode__(self):
		       return str(self.apparel_id)



class ApparelFollow(models.Model):
	     apparel_id = models.IntegerField()
	     merchant_id = models.IntegerField()
	     device = models.CharField(max_length=1000)
	     #0 for laptop 1 for mobile 2 for tablet
	     os = models.CharField(max_length=1000)
	     browser = models.CharField(max_length=1000)
	     date = models.DateTimeField()
	     IP = models.IPAddressField()
	     country = models.CharField(max_length=1000)
	     user_followed_id = models.IntegerField(default=0)
	     user_shared_id = models.IntegerField()
	     followed_on = models.IntegerField()

	     def __unicode__(self):
		     return str(self.apparel_id)
	     

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
