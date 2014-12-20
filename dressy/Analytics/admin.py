from django.contrib import admin
from Analytics.models import UserProfile
from Analytics.models import ApparelTry, ApparelShare, ApparelFollow
admin.site.register(ApparelTry)
admin.site.register(ApparelShare)
admin.site.register(ApparelFollow)
# Register your models here.
admin.site.register(UserProfile)
