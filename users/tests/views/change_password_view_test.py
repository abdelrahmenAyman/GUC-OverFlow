from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse

from users.factories import UserFactory


class ChangePasswordViewTestSuite(APITestCase):
    """Author: Abdelrahmen Ayman"""

    def setUp(self):
        self.logged_in_user = UserFactory.create()
        self.logged_in_user.set_password('password')
        self.logged_in_user.save()
        self.client.force_login(self.logged_in_user)

        self.change_password_path = reverse('change-password')
        self.change_password_data = {
            'old_password': 'password',
            'new_password': 'new password',
            'confirm_password': 'new password'
        }

    def test_request_should_be_authenticated(self):
        client = APIClient()
        response = client.post(
            path=self.change_password_path, data=self.change_password_data)

        self.assertEqual(403, response.status_code)

    def test_old_password_missing(self):
        del self.change_password_data['old_password']
        response = self.client.post(
            path=self.change_password_path, data=self.change_password_data)

        self.assertEqual(400, response.status_code)

    def test_new_password_missing(self):
        del self.change_password_data['new_password']
        response = self.client.post(
            path=self.change_password_path, data=self.change_password_data)

        self.assertEqual(400, response.status_code)

    def test_confirm_password_missing(self):
        del self.change_password_data['confirm_password']
        response = self.client.post(
            path=self.change_password_path, data=self.change_password_data)

        self.assertEqual(400, response.status_code)

    def test_wrong_old_password(self):
        self.change_password_data['old_password'] = 'wrong password'
        response = self.client.post(
            path=self.change_password_path, data=self.change_password_data)

        self.assertEqual(400, response.status_code)
        self.assertFalse(
            self.logged_in_user.check_password(
                self.change_password_data['new_password'])
        )

    def test_new_password_and_confirm_password_not_matching(self):
        self.change_password_data['confirm_password'] = 'not matching password'
        response = self.client.post(
            path=self.change_password_path, data=self.change_password_data)

        self.assertEqual(400, response.status_code)
        self.assertFalse(
            self.logged_in_user.check_password(
                self.change_password_data['new_password'])
        )

    def test_change_password_successfully(self):
        response = self.client.post(
            path=self.change_password_path, data=self.change_password_data)
        self.logged_in_user.refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertTrue(self.logged_in_user.check_password(
            self.change_password_data['new_password']))
