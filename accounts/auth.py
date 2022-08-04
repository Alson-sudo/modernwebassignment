# who access what, I decide
from django.shortcuts import redirect
# to check if the user is logged in or not


def unauthenticated_user(view_function):
    def wrapper_fxn(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/collection/homepage')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_fxn

# check if user is admin? if user=admin, gives access to admin panel
# user not = admin, redirects to user dashboard


def admin_only(view_function):
    def wrapper_fxn(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('/collection/homepage')
    return wrapper_fxn

# check if user is normal(not admin)
# if user not = admin , access user page
# if user = admin, redirects admin dashboard


def user_only(view_function):
    def wrapper_fxn(request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect('/admins/admin-home')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_fxn

