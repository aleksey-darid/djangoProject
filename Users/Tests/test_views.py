from django.contrib.auth.models import User, Group
from django.test import TestCase, Client

from Users.models import WorkersModel


class UsersTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_HomeViews(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_OrderViews(self):
        response = self.client.get('/order_page/')
        self.assertEqual(response.status_code, 200)

    def test_UsersViews(self):
        response = self.client.get('/users_page/')
        self.assertEqual(response.status_code, 200)

    def test_WorkersViews(self):
        response = self.client.get('/workers_page/')
        self.assertEqual(response.status_code, 200)
        User.objects.create(username="test", password="test", id=1)
        user2 = User.objects.create(username="test1", password="test1", id=2)
        Group.objects.create(name='Workers')
        response_post = self.client.post('/workers_add/', {"add": "add", "name": 1, "pay": 5})
        self.assertEqual(response_post.status_code, 302)
        WorkersModel.objects.create(id=2, user=user2, rate_per_hour=5)
        response_post = self.client.post('/workers_put/', {"put": "put", "id": 2, "pay": 4})
        self.assertEqual(response_post.status_code, 302)
        Group.objects.create(name='Users')
        response_post = self.client.post('/workers_del/', {"del": "del", "del_name": 2})
        self.assertEqual(response_post.status_code, 302)

    def test_LoginViews(self):
        response = self.client.get('/login_page/')
        self.assertEqual(response.status_code, 200)
        response_post = self.client.post('/login_page/', {"username": "aleksey", "password": "postgres"})
        self.assertEqual(response_post.status_code, 200)

    def test_LogoutViews(self):
        response = self.client.get('/logout_page/')
        self.assertEqual(response.status_code, 200)
        response_post = self.client.post('/logout_page/')
        self.assertEqual(response_post.status_code, 302)

    def test_RegistrationViews(self):
        response_post = self.client.post('/registration_page/')
        self.assertEqual(response_post.status_code, 200)
