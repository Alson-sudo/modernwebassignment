from django.test import SimpleTestCase
from django.urls import reverse, resolve
from collection.views import *


class TestsUrls(SimpleTestCase):

    def test_list_url_homepage(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, homepage)

    def test_list_url_collect_name(self):
        url = reverse('collect_form')
        print(resolve(url))
        self.assertEquals(resolve(url).func, collection_form)

    def test_list_url_collection(self):
        url = reverse('user_collection')
        print(resolve(url))
        self.assertEquals(resolve(url).func, user_collection)

    def test_list_url_upload(self):
        url = reverse('upload')
        print(resolve(url))
        self.assertEquals(resolve(url).func, upload)

    def test_list_url_artists(self):
        url = reverse('artist')
        print(resolve(url))
        self.assertEquals(resolve(url).func, artist)


