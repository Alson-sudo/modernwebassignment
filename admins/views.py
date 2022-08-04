from django.shortcuts import render, redirect
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from collection.models import *
from accounts.models import *

@login_required
@admin_only
def dashboard(request):
        beats = Wallpaper.objects.all()
        beats_count = beats.count()
        category = Collection.objects.all()
        category_count = category.count()
        feedback= Feedback.objects.all()
        feedback_count = feedback.count()
        user = User.objects.filter(is_staff=0)
        user_count = user.count()
        admin = User.objects.filter(is_staff=1)
        admin_count = admin.count()

        context = {
            'beats': beats_count,
            'category': category_count,
            'feedback': feedback_count,
            'user': user_count,
            'admin': admin_count,

        }
        return render(request, 'admins/dashboard.html', context)


@login_required
@admin_only
def show_users(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    context = {
        'users': users,
        'activate_users':'active'
    }
    return render(request,'admins/users.html',context)


@login_required
@admin_only
def show_admins(request):
    admins = User.objects.filter(is_staff=1).order_by('-id')
    context = {
        'admins':admins,
        'activate_admins': 'active'
    }
    return render(request,'admins/admins.html',context)


@login_required
@admin_only
def promote_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request,messages.SUCCESS,'User promoted to admin')
    return redirect('/admins/admins')


@login_required
@admin_only
def demote_admin(request,user_id):
    admin = User.objects.get(id=user_id)
    admin.is_staff = False
    admin.save()
    messages.add_message(request,messages.SUCCESS,'admin demoted to user')
    return redirect('/admins/users')


@login_required
@admin_only
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request,messages.SUCCESS, 'User Deleted Successfully')
    return redirect('/admins/users')


@login_required
@admin_only
def delete_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request,messages.SUCCESS, 'Admin Deleted Successfully')
    return redirect('/admins/admins')