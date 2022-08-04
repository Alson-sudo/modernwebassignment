from django.urls import path, include

urlpatterns = [
    path('collection/', include('collection.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls'))
]
