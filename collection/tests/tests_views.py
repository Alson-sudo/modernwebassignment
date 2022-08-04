# from django.test import  TestCase, Client
# from django.urls import reverse
# from collection.models import Collection, Wallpaper, Feedback
# import json
#
# class TestViews(TestCase):
#
#
#     def setUp(self):
#         self.client = Client()
#         self.list_url = reverse('feeder')
#         self.list_url = reverse('collect_form')
#         Feedback.objects.create(
#             name='project1',
#
#         )
#
#     # def test_user_feedback(self):
#     #     response = self.client.get(reverse('feeder'))
#     #
#     #     self.assertEquals(response.status_code, 200)
#     #     self.assertTemplateUsed(response, 'collection/feedback_form.html')
#
#     def test_user_feedback(self):
#         Feedback.objects.create(
#             project=self.
#         )
#
#     def test_collection_form(self):
#         response = self.client.get(reverse('collect_form'))
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'collection/collection_form.html')
#
