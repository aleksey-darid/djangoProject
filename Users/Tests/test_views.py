from django.test import TestCase, Client


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

    def test_Workers_addViews(self):
        response = self.client.get('/workers_add/')
        self.assertEqual(response.status_code, 200)
        response_post = self.client.post('/workers_add/')
        self.assertEqual(response_post.status_code, 200)

    def test_Workers_delViews(self):
        response = self.client.get('/workers_del/')
        self.assertEqual(response.status_code, 200)
        response_post = self.client.post('/workers_del/')
        self.assertEqual(response_post.status_code, 200)

    def test_Workers_putViews(self):
        response = self.client.get('/workers_put/')
        self.assertEqual(response.status_code, 200)
        response_post = self.client.post('/workers_put/')
        self.assertEqual(response_post.status_code, 200)

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
