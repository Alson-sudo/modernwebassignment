from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='home'),

    path('collection_get', views.collection_get),
    path('collection_form', views.collection_form, name='collect_form'),
    path('collection_delete/<int:collection_id>', views.collection_delete),
    path('collection_update/<int:collection_id>', views.collection_update),

    path('wallpaper_get', views.wallpaper_get),
    path('wallpaper_form', views.wallpaper_form),
    path('wallpaper_delete/<int:wallpaper_id>', views.wallpaper_delete),
    path('wallpaper_update/<int:wallpaper_id>', views.wallpaper_update),

    path('user_collection', views.user_collection, name='user_collection'),
    path('user_wallpaper', views.user_wallpaper),


    path('feedback', views.user_feedback, name='feeder'),
    path('show_feedback', views.show_feedback),
    path('done_feedback/<int:feedback_id>', views.done_feedback),

    path('upload', views.upload, name='upload'),

    path('artist', views.artist, name='artist'),
    path('artist_profile', views.artistprofile),

    path('add_to_cart/<int:wallpaper_id>', views.add_to_cart),
    path('remove_cart_item/<int:cart_id>', views.remove_cart_item),
    path('mycart', views.show_cart_items),
    path('my_order/<int:wallpaper_id>/<int:cart_id>', views.order),
    path('my_order', views.my_order),



    path('get_product_beats', views.show_product_beats, name='show_product_beats'),
    path('get_genre_beats', views.test_genre, name='show_genre_beats'),

]
