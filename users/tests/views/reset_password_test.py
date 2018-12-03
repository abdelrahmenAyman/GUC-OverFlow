from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from users.factories import GucianFactory


class ResetPasswordViewTestSuite(APITestCase):
    """Author: Abdelrahmen Ayman"""

    def setUp(self):
        self.gucian = GucianFactory.create()

        self.reset_password_path = reverse(
            'reset-password', kwargs={'pk': self.gucian.pk})
        self.reset_password_data = {
            'new_password': 'password',
            'confirm_password': 'password'
        }

    def test_new_password_missing(self):
        del self.reset_password_data['new_password']
        response = self.client.put(
            path=self.reset_password_path,
            data=self.reset_password_data)

        self.assertEqual(400, response.status_code)

    def test_confirm_password_missing(self):
        del self.reset_password_data['confirm_password']
        response = self.client.put(
            path=self.reset_password_path,
            data=self.reset_password_data)

        self.assertEqual(400, response.status_code)

    def test_provided_passwords_not_equal(self):
        self.reset_password_data['confirm_password'] = 'not matching password'
        response = self.client.put(
            path=self.reset_password_path,
            data=self.reset_password_data)

        self.assertEqual(400, response.status_code)

    def test_reset_password_successful(self):
        response = self.client.put(
            path=self.reset_password_path,
            data=self.reset_password_data)
        self.gucian.user.refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertTrue(
            self.gucian.user.check_password(
                self.reset_password_data['new_password']))
