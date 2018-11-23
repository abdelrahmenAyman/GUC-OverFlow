import datetime

from django.test import TestCase

from ..factories import GucianFactory


class GucianTestSuite(TestCase):
    """Author: Abdelrahmen Ayman"""

    def setUp(self):
        self.gucian = GucianFactory.create()

    def test_age_representation(self):
        self.assertEqual(
            datetime.datetime.now().year - self.gucian.birthdate.year,
            self.gucian.age
        )

    def test_name_representation(self):
        self.assertEqual(
            f'{self.gucian.user.first_name} {self.gucian.user.last_name}',
            self.gucian.name
        )

    def test_string_representation(self):
        self.assertEqual(self.gucian.name, str(self.gucian))
