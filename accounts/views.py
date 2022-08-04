from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, ProfilesForm
from accounts.auth import unauthenticated_user, admin_only, user_only
from django.contrib.auth.decorators import login_required
from .models import Profiles
from .filter import ArtistsFilter
from collection.models import Wallpaper
from django.contrib.auth import update_session_auth_hash
import os


def homepage(request):
    return render(request, 'accounts/homepage.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('/admins/dashboard')
                elif not user.is_superuser:
                    login(request, user)
                    return redirect('/collection/user_wallpaper')

            else:
                messages.add_message(request, messages.ERROR, "Invalid user")
                return render(request, 'accounts/login.html', {'form_login': form})
    context = {
        'form_login': LoginForm,
        'active_login': 'active'
    }
    return render(request, 'accounts/login.html', context)


@unauthenticated_user
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User registered successfully')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to register!')
            return render(request, 'accounts/register.html', {'form_register': form})
    context = {
        'form_register': UserCreationForm,
        'active_register': 'active'
    }
    return render(request, 'accounts/register.html', context)
# Create your views here.

@login_required
@user_only
def profile_update(request):
    profiles, created = Profiles.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfilesForm(request.POST, request.FILES, instance=profiles)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile updated successfully')
            return redirect('/profile')
    context = {
        'form':ProfilesForm(instance=profiles),
        'activate_profile':'active',
    }
    return render(request, 'accounts/profile_update.html', context)


@login_required
@user_only
def profile(request):
    profile, created = Profiles.objects.get_or_create(user=request.user)
    artists_id = request.user
    posts = Wallpaper.objects.filter(user=artists_id)

    context = {
        'activate_profile': 'active',
        'posts': posts,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
@user_only
def show_artists(request):
    artists = User.objects.filter(is_staff=0)
    artists_filter = ArtistsFilter(request.GET, queryset=artists)
    artists_final = artists_filter.qs
    context = {
        'artists':artists_final,
        'activate_artists':'active',
        'artists_filter':artists_filter,
    }
    return render(request,'accounts/show_artists.html',context)


@login_required
@user_only
def show_profile_artists(request):
    artists = request.GET.get('artists')
    artists_id = User.objects.get(username=artists).pk
    if artists == None:
        profile = User.objects.order_by('-id').filter(is_published=True)
    else:
        profile = User.objects.filter(username=artists)
        posts = Wallpaper.objects.filter(user=artists_id)

    profile_artists = User.objects.filter(is_staff=0)
    context = {
        'profile':profile,
        'posts': posts,
        'profile_artists': profile_artists,
    }
    return render(request, 'accounts/show_profile_artists.html', context)


@login_required
@user_only
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.add_message(request, messages.SUCCESS,'Password Changed Successfully')
            return redirect('/profile')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify the form fields')
            return render(request,'accounts/password_change.html',{'password_change_form':form})
    context = {
        'password_change_form':PasswordChangeForm(request.user),
        'activate_settings':'active',
    }

    return render(request,'accounts/password_change.html',context)


@login_required
@user_only
def delete_music(request, wallpaper_id):
    beats = Wallpaper.objects.get(id=wallpaper_id)
    os.remove(beats.wall_img.path)
    beats.delete()
    messages.add_message(request, messages.SUCCESS, 'Wallpaper Deleted Successfully')
    return redirect('/profile')








