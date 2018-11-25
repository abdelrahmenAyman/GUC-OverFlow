import datetime

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from django.contrib.auth import get_user_model

from users.models import Gucian

User = get_user_model()


class SignUpViewTestSuite(APITestCase):
    """Author: Abdelrahmen Ayman"""

    def setUp(self):
        self.signup_path = reverse('signup')
        self.signup_data = {
            'first_name': 'Abdelrahmen',
            'last_name': 'Ayman',
            'guc_email': 'abdelrahmen@student.guc.edu.eg',
            'backup_email': 'abdelrahmen@gmail.com',
            'major': 'MET',
            'dash_number': 37,
            'birthdate': str(datetime.date(1997, 6, 28)),
            'bio': 'The best developer ever',
            'password': 'password',
            'confirm_password': 'password'
        }

    def test_first_name_missing(self):
        del self.signup_data['first_name']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(400, response.status_code)

    def test_last_name_missing(self):
        del self.signup_data['last_name']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(400, response.status_code)

    def test_guc_email_missing(self):
        del self.signup_data['guc_email']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(400, response.status_code)

    def test_backup_email_missing(self):
        del self.signup_data['backup_email']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(400, response.status_code)

    def test_major_missing(self):
        del self.signup_data['major']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(400, response.status_code)

    def test_dash_number_missing(self):
        del self.signup_data['dash_number']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(400, response.status_code)

    def test_birthdate_missing(self):
        del self.signup_data['birthdate']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(400, response.status_code)

    def test_password_missing(self):
        del self.signup_data['password']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(400, response.status_code)

    def test_confirm_password_missing(self):
        del self.signup_data['confirm_password']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(400, response.status_code)

    def test_bio_missing_is_allowed(self):
        del self.signup_data['bio']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data)

        self.assertEqual(200, response.status_code)

    def test_guc_email_does_not_include_guc_domain(self):
        self.signup_data['guc_email'] = 'whatever@whatever.com'

        response = self.client.post(
            path=self.signup_path, data=self.signup_data
        )

        self.assertEqual(400, response.status_code)

    def test_birthdate_can_not_be_before_1930(self):
        self.signup_data['birthdate'] = datetime.date(1929, 1, 1)

        response = self.client.post(
            path=self.signup_path, data=self.signup_data
        )

        self.assertEqual(400, response.status_code)

    def test_age_can_not_be_less_than_16(self):
        now = datetime.datetime.now()
        birthdate_year = now.year - 15
        self.signup_data['birthdate'] = datetime.date(birthdate_year, 1, 1)

        response = self.client.post(
            path=self.signup_path, data=self.signup_data
        )

        self.assertEqual(400, response.status_code)

    def test_backup_email_not_equal_guc_email(self):
        self.signup_data['backup_email'] = self.signup_data['guc_email']

        response = self.client.post(
            path=self.signup_path, data=self.signup_data
        )

        self.assertEqual(400, response.status_code)

    def test_gucian_created_on_sign_up(self):
        self.client.post(
            path=self.signup_path, data=self.signup_data
        )

        self.assertEqual(1, Gucian.objects.count())
