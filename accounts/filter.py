import django_filters
from .models import Profiles
# from django.contrib.auth.models import User


class ArtistsFilter(django_filters.FilterSet):
    name_contains = django_filters.CharFilter(field_name = 'username', lookup_expr='icontains')
    class Meta:
        model = Profiles
        fields = []