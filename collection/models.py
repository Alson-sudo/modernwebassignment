from django.db import models
from django.core.validators import *
from django.core import validators
from django.contrib.auth.models import User


class Collection(models.Model):
    collection_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    collection_desc = models.TextField(null=True)
    collection_img = models.FileField(upload_to='static/uploads', null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

# foreign key shown in dropdown

    def __str__(self):
        return self.collection_name
# Create your models here.


class Wallpaper(models.Model):
    wallpaper_name = models.CharField(max_length=200)
    wallpaper_price = models.FloatField()
    wall_img = models.FileField(upload_to='static/uploads')
    # CASCADE deletes certain collection
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.wall_name


class Carts(models.Model):
    wallpaper = models.ForeignKey(Wallpaper, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):

    message = models.TextField()
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)


class Order(models.Model):
    STATUS = (
        ('Bought', 'Bought'),
    )
    wallpaper = models.ForeignKey(Wallpaper, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    total_price = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)


