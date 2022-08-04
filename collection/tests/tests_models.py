from django.test import TestCase
from collection.models import Collection, Wallpaper


class TestModels(TestCase):

    def setUp(self):
        self.test1 = Wallpaper.objects.create(
            wallpaper_name='test 1',
            wallpaper_price=694.20,
        )


