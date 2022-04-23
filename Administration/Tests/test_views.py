from django.test import TestCase


class AdministrationTestCase(TestCase):

    def test_BidViews(self):
        response = self.client.get('/bid_page/')
        self.assertEqual(response.status_code, 200)
        response_post = self.client.post('/bid_page/')
        self.assertEqual(response_post.status_code, 302)

    def test_ScheduleViews(self):
        response = self.client.get('/schedule_page/')
        self.assertEqual(response.status_code, 200)
        response_post = self.client.post('/schedule_page/')
        self.assertEqual(response_post.status_code, 302)
