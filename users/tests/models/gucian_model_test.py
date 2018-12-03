import datetime

from django.test import TestCase

from users.factories import GucianFactory


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

    def test_increase_reputation(self):
        """Tests the mechanism of increasing reputation"""
        reputation_before_increasing = self.gucian.reputation
        self.gucian.increase_reputation(amount=5)
        self.gucian.refresh_from_db()

        self.assertEqual(reputation_before_increasing +
                         5, self.gucian.reputation)

    def test_decrease_reputation(self):
        """Tests the mechanism of decreasing reputation"""
        reputation_before_increasing = self.gucian.reputation
        self.gucian.decrease_reputation(amount=1)
        self.gucian.refresh_from_db()

        self.assertEqual(reputation_before_increasing -
                         1, self.gucian.reputation)
