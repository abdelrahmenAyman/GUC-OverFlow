from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from users.factories import GucianFactory


class GucianViewSetTestSuite(APITestCase):
    """Author: Abdelrahmen Ayman"""

    def setUp(self):
        self.gucians = GucianFactory.create_batch(10)

        self.path = reverse('gucian-detail', kwargs={'pk': 1})
        self.update_data = {'bio': 'New bio'}

        self.client.force_login(self.gucians[0].user)

    def test_retrieve_non_existing_gucian(self):
        path_to_non_existing = reverse('gucian-detail', kwargs={'pk': 100})
        response = self.client.get(path=path_to_non_existing)

        self.assertEqual(404, response.status_code)

    def test_retrieve_existing_gucian(self):
        response = self.client.get(path=self.path)
        self.assertEqual(200, response.status_code)

    def test_update_not_profile_owner(self):
        self.client.logout()
        self.client.force_login(self.gucians[1].user)

        response = self.client.patch(path=self.path, data=self.update_data)

        self.assertEqual(403, response.status_code)

    def test_update_successfully(self):
        response = self.client.patch(path=self.path, data=self.update_data)
        self.gucians[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            self.update_data['bio'],
            self.gucians[0].bio)

    def test_edit_first_name_successfully(self):
        del self.update_data['bio']
        self.update_data['first_name'] = 'Aya'

        response = self.client.patch(path=self.path, data=self.update_data)
        self.gucians[0].user.refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            self.update_data['first_name'],
            self.gucians[0].user.first_name
        )
