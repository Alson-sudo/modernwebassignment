import django_filters
from .models import Wallpaper


class WallpaperFilter(django_filters.FilterSet):
    name_contains = django_filters.CharFilter(field_name = 'wallpaper_name', lookup_expr='icontains')

    class Meta:
        model = Wallpaper
        fields = []

