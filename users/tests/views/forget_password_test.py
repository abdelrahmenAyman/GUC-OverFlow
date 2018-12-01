from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from django.core import mail

from users.factories import GucianFactory


class ForgetPasswordViewTestSuite(APITestCase):
    """Author: Abdelrahmen Ayman"""

    def setUp(self):
        self.gucian = GucianFactory.create()

        self.forget_password_path = reverse('forget-password')
        self.forget_password_data = {'email': self.gucian.guc_email}

    def test_given_email_does_not_exist(self):
        self.forget_password_data['email'] = 'non_existing@example.com'
        response = self.client.post(
            path=self.forget_password_path, data=self.forget_password_data)

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(mail.outbox))

    def test_missing_email_field(self):
        del self.forget_password_data['email']
        response = self.client.post(
            path=self.forget_password_path, data=self.forget_password_data)

        self.assertEqual(400, response.status_code)

    def test_forget_password_successfully(self):
        response = self.client.post(
            path=self.forget_password_path, data=self.forget_password_data)

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(mail.outbox))
