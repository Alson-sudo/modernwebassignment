from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    description = models.TextField()
    profile_pic = models.FileField(upload_to='static/profile', default = 'static/img/clown.jpg')
    created_date = models.DateTimeField(auto_now_add=True)



