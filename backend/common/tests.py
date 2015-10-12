from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.conf import settings
from django.utils.dateparse import parse_datetime
from rest_framework import ISO_8601
from rest_framework.test import APITestCase
from .filters import IsoDateTimeField


class LoginMixin(object):

    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            email='tester@pos.co.ke',
            first_name='Test',
            last_name='Test',
            password='tester'
        )
        login_url = settings.LOGIN_URL
        login_data = {
            'username': 'tester@pos.co.ke', 'password': 'tester'
        }
        response = self.client.post(login_url, login_data)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(response.data['key']))
        self.maxDiff = None
        super(LoginMixin, self).setUp()


class TestIsoDateTimeField(LoginMixin, APITestCase):
    def test_strp_time_valid_iso_date(self):
        fl = IsoDateTimeField()
        valid_iso_date = '2015-04-14T06:46:32.709388Z'
        self.assertTrue(fl.strptime(valid_iso_date, ISO_8601))
        self.assertEquals(
            fl.strptime(value=valid_iso_date, format=ISO_8601),
            parse_datetime(valid_iso_date)
        )

    def test_strp_time_invalid_iso_date(self):
        fl = IsoDateTimeField()
        invalid_iso_date = 'random stuff'
        with self.assertRaises(ValueError):
            fl.strptime(value=invalid_iso_date, format=ISO_8601)

    def test_strp_time_fallback(self):
        fl = IsoDateTimeField()
        # Should fall back uneventfully
        fl.strptime(
            value='2006-10-25 14:30:59', format='%Y-%m-%d %H:%M:%S')
