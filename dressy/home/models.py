from django.db import models

# Create your models here.
class Apparel(models.Model):

	price = models.IntegerField(default=1000)
	merchant_id = models.IntegerField(default=0)
	image = models.ImageField(upload_to="upload/")

	def __unicode__(self):
		return str(self.id)
