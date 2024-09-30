from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
# User Profiles
class UserProfile(models.Model):
    FEMALE = 'FEMALE'
    MALE = 'MALE'

    CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    ]
    name = models.CharField(max_length=300)
    email = models.EmailField()
    username = models.CharField(max_length=300)
    phone = models.CharField(max_length=50, null=True, blank=True)
    # picture = models.ImageField(upload_to='image/', default='blank-profile-picture.png', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=CHOICES, default=FEMALE)
    date_of_birth = models.DateField(verbose_name=('date_of_birth'), null=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username