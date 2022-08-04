from django.shortcuts import render, redirect
from . forms import CollectionForm, WallpaperForm, FeedbackForm
from django.contrib import messages
from .models import Collection, Wallpaper, Carts, Feedback, Order
from accounts.auth import admin_only, user_only
# Create your views here.
from django.contrib.auth.decorators import login_required
import os
from .filter import *


@login_required
@admin_only
def collection_form(request):
    if request.method == "POST":
        form = CollectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Added to collection')
            return redirect('/collection/collection_get')
        else:
            messages.add_message(request, messages.ERROR, 'Fail to add in collection')
            return render(request, 'collection/collection_form.html', {'form_collection': form})
    context = {
        'form_collection': CollectionForm,
        'active_collection': 'active',
    }
    return render(request, 'collection/collection_form.html', context)


@login_required
@admin_only
def collection_get(request):
    collection = Collection.objects.all().order_by('-id')
    context = {
        'collection_key': collection,
        'active_collection': 'active'
    }
    return render(request, 'collection/collection_get.html', context)


@login_required
@admin_only
def collection_delete(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    collection.delete()
    messages.add_message(request, messages.ERROR, 'Collection Deleted')
    return redirect('/collection/collection_get')


@login_required
@user_only
def homepage(request):
    return render(request, 'collection/homepage.html')


@login_required
@admin_only
def collection_update(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    if request.method == "POST":
        form = CollectionForm(request.POST, request.FILES, instance=collection)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Collection Updated')
            return redirect('/collection/collection_get')
        else:
            messages.add_message(request, messages.ERROR, 'Fail to update collection')
            return render(request, 'collection/collection_update_form.html', {'form_collection': form})
    context = {
        'form_collection': CollectionForm(instance=collection),
        'active_collection': 'active',
    }
    return render(request, 'collection/collection_update_form.html', context)


@login_required
@admin_only
def wallpaper_form(request):
    if request.method == "POST":
        form = WallpaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Added to wallpaper')
            return redirect('/collection/wallpaper_get')
        else:
            messages.add_message(request, messages.ERROR, 'Fail to add wallpaper')
            return render(request, 'wallpaper/wallpaper_form.html', {'form_wallpaper': form})
    context = {
        'form_wallpaper': WallpaperForm,
        'active_wallpaper': 'active',
    }
    return render(request, 'wallpaper/wallpaper_form.html', context)


@login_required
@admin_only
def wallpaper_get(request):
    wallpaper = Wallpaper.objects.all().order_by('-id')

    context = {
        'wallpaper_key': wallpaper,
        'active_wallpaper': 'active'
    }
    return render(request, 'wallpaper/wallpaper_get.html', context)


@login_required
@admin_only
def wallpaper_delete(request, wallpaper_id):
    wallpaper = Wallpaper.objects.get(id=wallpaper_id)
    wallpaper.delete()
    # to delete wallpaper
    os.remove(wallpaper.wall_img.path)
    messages.add_message(request, messages.ERROR, 'Wallpaper Deleted')
    return redirect('/collection/wallpaper_get')


@login_required
@admin_only
def wallpaper_update(request, wallpaper_id):
    wallpaper = Wallpaper.objects.get(id=wallpaper_id)
    if request.method == "POST":
        form = WallpaperForm(request.POST, request.FILES, instance=wallpaper)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Wallpaper Updated')
            return redirect('/collection/wallpaper_get')
        else:
            messages.add_message(request, messages.ERROR, 'Fail to update wallpaper')
            return render(request, 'wallpaper/wallpaper_update_form.html', {'form_wallpaper': form})
    context = {
        'form_wallpaper': WallpaperForm(instance=wallpaper),
        'active_wallpaper': 'active',
    }
    return render(request, 'wallpaper/wallpaper_update_form.html', context)


def user_collection(request):
    collection = Collection.objects.all().order_by('collection_name')
    context = {
        'collection': collection,
        'active_collection_user': 'active'
    }
    return render(request, 'collection/user_collection.html', context)


def user_wallpaper(request):
    wallpaper = Wallpaper.objects.all().order_by('-id')
    wallpaper_filter = WallpaperFilter(request.GET, queryset=wallpaper)
    wallpaper_final = wallpaper_filter.qs
    context = {
        'wallpaper': wallpaper_final,
        'active_wallpaper_user': 'active',
        'wallpaper_filter': wallpaper_filter,
    }
    return render(request, 'wallpaper/user_wallpaper.html', context)


# def menu(request):
#     collection = Collection.objects.all().order_by('-id')
#     context = {
#         'collection': collection,
#         'active_menu': 'active'
#     }
#     return render(request, 'collection/menu.html', context)




@login_required
@user_only
def add_to_cart(request, wallpaper_id):
    user = request.user
    beats = Wallpaper.objects.get(id=wallpaper_id)
    # cart = Cart.objects.create(beats=beats, user=user)

    check_item_presence = Carts.objects.filter(user=user, wallpaper=beats)
    if check_item_presence:
        messages.add_message(request, messages.ERROR, 'Item is already present in cart')
        return redirect('/collection/user_wallpaper')
    else:
        cart = Carts.objects.create(wallpaper=beats, user=request.user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Item added to cart')
            return redirect('/collection/user_wallpaper')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add to item to cart')


@login_required
@user_only
def show_cart_items(request):
    user = request.user
    items = Carts.objects.filter(user=user)
    context = {
        'items': items,
        'activate_my_cart': 'active'
    }
    return render(request, 'beats/cart.html', context)


@login_required
@user_only
def remove_cart_item(request, cart_id):
    item = Carts.objects.get(id=cart_id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Cart item removed successfully')
    return redirect('/collection/mycart')



@login_required
@user_only
def user_feedback(request):
    form = FeedbackForm(request.POST)
    if request.method == "POST":
        form = FeedbackForm(request.POST,)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.owner = request.user
            task_list.save()
            # form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully')
            return redirect('/collection/feedback')
        else:
            messages.add_message(request,messages.ERROR, 'Unable to add')
            return render(request,'beats/feedback_form', {'form_feedback' : form})
    context={
        'form_feedback': FeedbackForm,
        'activate_feedback': 'active',
    }
    return render(request, 'beats/feedback_form.html', context)

@login_required
@admin_only
def show_feedback(request):
    feedback = Feedback.objects.all().order_by('-id')
    context = {
        'feedback': feedback,
        'activate_feedback': 'active',
    }
    return render(request, 'beats/show_feedback.html', context)

@login_required
@admin_only
def done_feedback(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    feedback.delete()
    messages.add_message(request,messages.SUCCESS, 'Done')
    return redirect('/collection/show_feedback')


@login_required
@user_only
def upload(request):
    if request.method == "POST":
        form = WallpaperForm(request.POST, request.FILES)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user
            task_list.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Uploaded Successfully')
            return redirect('/profile')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to upload')
            return render(request, 'beats/beats_form.html', {'form_uploads': form})
    context = {
        'form_uploads': WallpaperForm,
        'activate_uploads': 'active',
    }
    return render(request, 'beats/upload_form.html', context)


@login_required
@user_only
def artist(request):
    context = {
        'active_artist': 'active',
    }
    return render(request, 'contact/artist.html', context)


@login_required
@user_only
def artistprofile(request):
    return render(request, 'contact/artistprofile.html')


def show_product_beats(request):
    product = request.GET.get('product')

    if product == None:
        beats = Wallpaper.objects.order_by('-id').filter(is_published=True)
    else:
        beats = Wallpaper.objects.filter(wallpaper_name=product)

    product_beats = Wallpaper.objects.all()
    context = {
        'beats': beats,
        'product_beats': product_beats
    }
    return render(request, 'beats/show_product_beats.html', context)


def test_genre(request):
    category = request.GET.get('category')
    if category == None:
        beats = Wallpaper.objects.order_by('-id').filter(is_published=True)
    else:
        beats = Wallpaper.objects.filter(collection__collection_name=category)
        cat = Collection.objects.filter(collection_name=category)
    categories = Collection.objects.all()
    context = {
        'beats': beats,
        'categories': categories,
        'cat':cat
    }
    return render(request, 'contact/testgenre.html', context)


@login_required
@user_only
def order(request, wallpaper_id, cart_id):
    user = request.user
    beats = Wallpaper.objects.get(id=wallpaper_id)
    cart_item = Carts.objects.get(id=cart_id)

    price = beats.wallpaper_price
    order = Order.objects.create(wallpaper=beats, user=user, total_price=price, status="Bought")
    if order:
        messages.add_message(request, messages.SUCCESS, 'Item Purchased')
        cart_item.delete()
        return redirect('/collection/my_order')
    else:
        messages.add_message(request, messages.ERROR, 'Something went wrong')
        return render(request, 'collection/my_order.html')

    context = {
        'order_form': OrderForm

    }
    return render(request, 'beats/my_order.html', context)


@login_required
@user_only
def my_order(request):
    user = request.user
    items = Order.objects.filter(user=user).order_by('-id')
    context = {
        'items': items,
        'activate_myorders': 'active'
    }
    return render(request, 'beats/my_order.html', context)
