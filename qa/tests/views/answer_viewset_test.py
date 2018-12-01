from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from qa.factories import AnswerFactory
from qa.models import Answer


class BaseAnswerTestSuite(APITestCase):
    """
    Base TestSuite to provide basic common setup for all Answer actions.
    """

    def setUp(self):
        self.answers = AnswerFactory.create_batch(10)

        self.list_path = reverse('answer-list')
        self.detail_path = reverse(
            'answer-detail', kwargs={'pk': self.answers[0].pk})

        self.client.force_login(self.answers[0].answerer.user)


class AnswerCreateViewTestSuite(BaseAnswerTestSuite):

    def setUp(self):
        super().setUp()
        self.create_data = {
            'text': 'New Answer',
            'question': 1,
        }

    def test_post_answer_missing_text(self):
        del self.create_data['text']
        response = self.client.post(
            path=self.list_path, data=self.create_data)

        self.assertEqual(400, response.status_code)

    def test_post_answer_missing_question(self):
        del self.create_data['question']
        response = self.client.post(
            path=self.list_path, data=self.create_data)

        self.assertEqual(400, response.status_code)

    def test_post_answer_to_non_existing_question(self):
        self.create_data['question'] = 100
        response = self.client.post(
            path=self.list_path, data=self.create_data)

        self.assertEqual(400, response.status_code)

    def test_post_answer_successfully(self):
        answerer = self.answers[0].answerer
        response = self.client.post(
            path=self.list_path, data=self.create_data)

        self.assertEqual(201, response.status_code)
        self.assertEqual(len(self.answers) + 1, Answer.objects.count())
        self.assertEqual(answerer.pk, response.data['answerer'])
