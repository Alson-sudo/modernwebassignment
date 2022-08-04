from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),

    path('users', views.show_users),
    path('admins', views.show_admins),

    path('promote/<int:user_id>', views.promote_user),
    path('demote/<int:user_id>', views.demote_admin),
    path('delete_users/<int:user_id>', views.delete_user),
    path('delete_admins/<int:user_id>', views.delete_admin),
]

