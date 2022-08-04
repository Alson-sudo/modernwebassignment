from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login', views.login_user),
    path('register', views.register_user),
    path('logout', views.logout_user),

    path('profile', views.profile),
    path('profile_update', views.profile_update),

    path('show_artists', views.show_artists),
    path('show_profile_artists', views.show_profile_artists, name='show_profile_artists'),

    path('change_password', views.change_password),
    path('delete_music/<int:wallpaper_id>', views.delete_music),

]