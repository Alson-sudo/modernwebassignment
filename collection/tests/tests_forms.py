from django.test import SimpleTestCase
from collection.forms import FeedbackForm, CollectionForm, WallpaperForm
# from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client


class TestForms(SimpleTestCase):

    def test_feedback_form(self):
        form = FeedbackForm(data={
            'message': 'Test messaging 123',
            'owner': '',
            'created_date': '',
        })

        self.assertTrue(form.is_valid())

    def test_feedback_incorrect_form(self):
        form = FeedbackForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    # def test_collection_form(self):
    #     form = CollectionForm(data={
    #         'collection_name': 'Abc',
    #         'collection_desc': 'killing in the name of',
    #         'collection_img': '',
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_collection_incorrect_form(self):
    #     form = CollectionForm(data={})
    #
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 3)



