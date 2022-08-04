from django import forms
from django.forms import ModelForm
from .models import Collection, Wallpaper, Feedback, Order


class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = "__all__"


class WallpaperForm(ModelForm):
    class Meta:
        model = Wallpaper
        fields = "__all__"
        exclude = ['user']


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ['owner']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['beats','user','total_price','status']
