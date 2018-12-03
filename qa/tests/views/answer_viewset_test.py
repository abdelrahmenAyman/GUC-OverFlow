from rest_framework.test import APITestCase, APIClient
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


class AnswerUpdateViewTestSuite(BaseAnswerTestSuite):

    def setUp(self):
        super().setUp()
        self.update_data = {
            'text': 'Different Text',
            'question': 3
        }

    def test_update_answerer(self):
        update_data = {'answerer': 10}
        response = self.client.patch(path=self.detail_path, data=update_data)
        self.answers[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(
            update_data['answerer'], self.answers[0].answerer.pk)

    def test_update_not_owner(self):
        client = APIClient()
        client.force_login(self.answers[4].answerer.user)

        response = client.patch(
            path=self.detail_path, data=self.update_data)

        self.assertEqual(403, response.status_code)

    def test_update_while_owner(self):
        response = self.client.patch(
            path=self.detail_path, data=self.update_data)
        self.answers[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.update_data['text'], self.answers[0].text)
        self.assertEqual(
            self.update_data['question'], self.answers[0].question.pk)


class AnswerVotingViewsTestSuite(BaseAnswerTestSuite):

    def setUp(self):
        super().setUp()
        self.up_vote_path = reverse(
            'answer-up-vote', kwargs={'pk': self.answers[0].pk})
        self.down_vote_path = reverse(
            'answer-down-vote', kwargs={'pk': self.answers[0].pk})

        self.client.logout()
        self.client.force_login(self.answers[1].answerer.user)

    def test_up_vote_non_existing_answer(self):
        non_existing_path = reverse('answer-up-vote', kwargs={'pk': 100})
        response = self.client.get(non_existing_path)

        self.assertEqual(404, response.status_code)

    def test_up_vote_answer(self):
        old_up_votes_count = self.answers[0].up_votes
        response = self.client.get(self.up_vote_path)
        self.answers[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(old_up_votes_count + 1, self.answers[0].up_votes)

    def test_down_vote_non_existing_answer(self):
        non_existing_path = reverse('answer-down-vote', kwargs={'pk': 100})
        response = self.client.get(non_existing_path)

        self.assertEqual(404, response.status_code)

    def test_down_vote_answer(self):
        old_down_votes_count = self.answers[0].down_votes
        response = self.client.get(self.down_vote_path)
        self.answers[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(old_down_votes_count + 1,
                         self.answers[0].down_votes)

    def test_increase_answer_answerer_reputation_on_a_up_vote(self):
        reputation_before_vote = self.answers[0].answerer.reputation
        response = self.client.get(self.up_vote_path)
        self.answers[0].answerer.refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(reputation_before_vote + 5,
                         self.answers[0].answerer.reputation)

    def test_decrease_answer_answerer_reputation_on_a_down_vote(self):
        reputation_before_vote = self.answers[0].answerer.reputation
        response = self.client.get(self.down_vote_path)
        self.answers[0].answerer.refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(reputation_before_vote - 1,
                         self.answers[0].answerer.reputation)

    def test_down_voter_loses_reputation(self):
        reputation_before_voting = self.answers[1].answerer.reputation
        response = self.client.get(self.down_vote_path)
        self.answers[1].answerer.refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(reputation_before_voting - 1,
                         self.answers[1].answerer.reputation)
