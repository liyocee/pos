from django.core.urlresolvers import reverse
from common.tests import LoginMixin
from rest_framework.test import APITestCase
from .models import User


class TestLogin(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='user@test.com',
            first_name='System',
            password='pass'
        )
        self.login_url = reverse("api:v1:rest_auth:rest_login")
        self.logout_url = reverse("api:v1:rest_auth:rest_logout")
        super(TestLogin, self).setUp()

    def test_login(self):
        data = {
            "username": 'user@test.com',
            "password": 'pass'
        }
        response = self.client.post(self.login_url, data)
        self.assertTrue(self.user.is_authenticated())
        self.assertEquals(200, response.status_code)
        self.assertTrue(
            response.data['user']['email'], self.user.email)

    def test_inactive_user_login(self):
        user = User.objects.create(
            email='user1@test.com',
            first_name='System',
            password='pass'
        )
        user.is_active = False
        user.save()
        response = self.client.post(
            self.login_url,
            {
                "username": user.email,
                "password": 'pass'
            }
        )
        self.assertEquals(400, response.status_code)
        self.assertEquals(
            {'non_field_errors': ['User account is disabled.']},
            response.data
        )

    def test_user_password_reset_success(self):
        user = User.objects.create(
            email='user1@test.com',
            first_name='System',
            password='pass'
        )
        user.is_active = False
        user.save()
        url = reverse("api:v1:rest_auth:rest_password_reset")
        response = self.client.post(url, {'email': user.email})
        self.assertEquals(200, response.status_code)
        self.assertTrue('success' in response.data)

    def test_user_password_reset_fail_non_existing_user(self):
        url = reverse("api:v1:rest_auth:rest_password_reset")
        response = self.client.post(url, {'email': 'hakuna@gmail.com'})
        self.assertEquals(400, response.status_code)
        self.assertFalse('success' in response.data)

    def test_login_user_does_not_exist(self):
        data = {
            "username": "non_existent@email.com",
            "password": 'pass'
        }
        response = self.client.post(self.login_url, data)
        self.assertEquals(400, response.status_code)
        self.assertEquals(
            {
                'non_field_errors': [
                    'Unable to log in with provided credentials.']
            },
            response.data
        )


class TestUserViews(LoginMixin, APITestCase):
    def test_create_user(self):
        create_url = reverse('api:v1:users:create')
        post_data = {
            "email": "user@healthix.co.ke",
            "first_name": "Hakuna",
            "last_name": "Ruhusa",
            "other_names": "",
            "password": "rubbishpass"
        }
        response = self.client.post(create_url, post_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual("Ruhusa", response.data["last_name"])

    def test_update_user(self):
        user = User.objects.create(
            email='user@test.com',
            first_name='System',
            password='pass'
        )
        update_url = reverse(
            'api:v1:users:user_detail', kwargs={'pk': user.id})
        patch_data = {
            "other_names": "Majina Mengine",
        }
        response = self.client.patch(update_url, patch_data)
        self.assertEqual(200, response.status_code)
        update_fail = self.client.patch(update_url, {'email': 'wrong'})
        self.assertEqual(update_fail.status_code, 400)

    def test_failed_create(self):
        create_url = reverse('api:v1:users:create')
        data = {
            "first_name": "yusa",
            "email": "yusa@yusa.com",
        }
        response = self.client.post(create_url, data)
        self.assertEqual(400, response.status_code)
