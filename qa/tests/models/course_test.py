from django.test import TestCase

from qa.factories import CourseFactory


class CourseTestSuite(TestCase):

    def setUp(self):
        self.course = CourseFactory()

    def test_str_representation(self):
        self.assertEqual(self.course.code, str(self.course))
