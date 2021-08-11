from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# Create your models here.

class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE) 
    image= models.URLField() ##to search about 
    image1= models.URLField(blank=True) 
    image2= models.URLField(blank=True) 
    image3= models.URLField(blank=True) 
    image4= models.URLField(blank=True) 
    discerption = models.TextField(null=True)
    comments = models.TextField(null=True)##to search about 
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Events(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE) 
    title= models.CharField(max_length=64)
    image= models.URLField(blank=True) 
    image1= models.URLField(blank=True) 
    image2= models.URLField(blank=True) 
    image3= models.URLField(blank=True) 
    image4= models.URLField(blank=True) 
    image5= models.URLField(blank=True) 
    image6= models.URLField(blank=True) 
    image7= models.URLField(blank=True) 
    image8= models.URLField(blank=True) 
    image9= models.URLField(blank=True) 
    image10= models.URLField(blank=True) 
    image11= models.URLField(blank=True) 
    image12= models.URLField(blank=True) 
    image13= models.URLField(blank=True) 
    image14= models.URLField(blank=True) 
    image15= models.URLField(blank=True) 
    image16= models.URLField(blank=True) 
    image17= models.URLField(blank=True) 
    image18= models.URLField(blank=True) 
    image19= models.URLField(blank=True) 
    image20= models.URLField(blank=True) 
    discerption = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class User(AbstractUser):
    username = models.CharField(max_length=64,unique=True)
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50 ,null=True, blank=True)
    photo = models.URLField(null=True,blank=True)
