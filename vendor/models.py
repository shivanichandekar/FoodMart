from django.db import models
from accounts.models import User,UserProfile
# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User, related_name= 'user', on_delete= models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name= 'userprofile', on_delete= models.CASCADE)
    Vendor_name = models.CharField(max_length= 50)
    # vendor_license = models.ImageField(upload_to= 'media/vendor/license')
    is_approved = models.BooleanField(default= False)
    modified_at = models.DateTimeField(auto_created=True)
    created_at = models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.Vendor_name