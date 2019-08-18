from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin,BaseUserManager
from django.conf import settings
# Create your models here.
#by default django has a self created user model that we use as a superuser but here we will make a custom made usermodel

class userprofile_manager(BaseUserManager):
    """manage for usermodel ,creating newuser authenticating them , and also do mention in the settings file otherwise will generate error"""
    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError("user must have an email address")
        email=self.normalize_email(email) #this will normalize the second portion of the email like GMAIL.COM written in capital will be converted into small letters
        user = self.model(email=email,name=name) #self.model mean userprofile
        user.set_password(password) #hashing the password
        user.save(using=self._db) #using=self._db is the best method to write otherwise we can also write user.save() just
        return user

    def create_superuser(self,name,email,password):
        user=self.create_user(name,email,password) #remember the sequence of the pass variables
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db) #using=self._db is the best method to write otherwise we can also write user.save() just
        return user



class userprofile(AbstractBaseUser,PermissionsMixin):
    """overwriting the usermodel making a custom one"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    # email=models.EmailField(max_length=255,unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name'] #this field does cause trouble remember


    objects=userprofile_manager()
    def get_user_name(self):
        return self.name


    def __str__(self):
        return self.email

user=settings.AUTH_USER_MODEL
class profilefeed_item(models.Model):
    user_profile=models.ForeignKey(user,on_delete=models.CASCADE)
    status_text=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.status_text
