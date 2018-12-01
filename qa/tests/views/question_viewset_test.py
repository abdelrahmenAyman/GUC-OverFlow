import datetime

from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse

from qa.factories import QuestionFactory, CourseFactory
from qa.models import Question

from users.factories import GucianFactory


class BaseQuestionTestSuite(APITestCase):
    """
    Base TestSuite to provide basic common setup for all Question actions.
    """

    def setUp(self):
        self.questions = QuestionFactory.create_batch(10)
        self.not_authenticated_client = APIClient()

        self.list_path = reverse('question-list')
        self.detail_path = reverse(
            'question-detail', kwargs={'pk': self.questions[0].pk})

        self.client.force_login(self.questions[0].asker.user)


class QuestionCreateViewTestSuite(BaseQuestionTestSuite):

    def setUp(self):
        super().setUp()

        self.create_data = {
            'course': self.questions[0].course.pk,
            'text': 'Question Text',
            'title': 'Question Title'
        }

    def test_create_question_not_authenticated(self):
        response = self.not_authenticated_client.post(
            path=self.list_path, data=self.create_data)

        self.assertEqual(403, response.status_code)

    def test_create_question_missing_text(self):
        del self.create_data['text']
        response = self.client.post(path=self.list_path, data=self.create_data)

        self.assertEqual(400, response.status_code)

    def test_create_question_missing_title(self):
        del self.create_data['title']
        response = self.client.post(path=self.list_path, data=self.create_data)

        self.assertEqual(400, response.status_code)

    def test_create_question_missing_course(self):
        del self.create_data['title']
        response = self.client.post(path=self.list_path, data=self.create_data)

        self.assertEqual(400, response.status_code)

    def test_create_question_successfully(self):
        old_questions_count = Question.objects.count()
        question_asker = self.questions[0].asker

        response = self.client.post(path=self.list_path, data=self.create_data)

        self.assertEqual(201, response.status_code)
        self.assertEqual(old_questions_count + 1, Question.objects.count())
        self.assertEqual(question_asker.pk, response.data['asker'])


class QuestionRetrieveViewTestSuite(BaseQuestionTestSuite):

    def test_retrieve_question_not_logged_in(self):
        response = self.not_authenticated_client.get(path=self.detail_path)

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.questions[0].text, response.data['text'])

    def test_retrieve_question_logged_in(self):
        response = self.client.get(path=self.detail_path)

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.questions[0].text, response.data['text'])

    def test_question_displays_its_answers_when_retrieved(self):
        response = self.client.get(path=self.detail_path)

        self.assertEqual(200, response.status_code)
        self.assertIn('answers', response.data.keys())

    def test_retrieve_question_not_existing(self):
        response = self.client.get(path=reverse(
            'question-detail', kwargs={'pk': 100}))
        self.assertEqual(404, response.status_code)


class QuestionListViewTestSuite(BaseQuestionTestSuite):

    def test_list_questions_not_logged_in(self):
        response = self.not_authenticated_client.get(path=self.list_path)

        self.assertEqual(200, response.status_code)
        self.assertEqual(len(self.questions), len(response.data))

    def test_list_questions_logged_in(self):
        response = self.not_authenticated_client.get(path=self.list_path)

        self.assertEqual(200, response.status_code)
        self.assertEqual(len(self.questions), len(response.data))

    def test_question_does_not_display_its_answers_when_listed(self):
        response = self.client.get(path=self.list_path)

        self.assertEqual(200, response.status_code)
        self.assertNotIn('answers', response.data[0].keys())


class QuestionUpdateViewTestSuite(BaseQuestionTestSuite):

    def setUp(self):
        super().setUp()

        self.course = CourseFactory()

        self.update_data = {
            'title': 'new title',
            'text': 'new text',
            'course': self.course.pk
        }

    def test_update_question_not_owner(self):
        gucian_not_owner = self.questions[1].asker
        client = APIClient()
        client.force_login(gucian_not_owner.user)

        response = client.patch(path=self.detail_path,
                                data={'title': 'New title'})

        self.assertEqual(403, response.status_code)

    def test_update_question_while_owner(self):
        response = self.client.put(
            path=self.detail_path, data=self.update_data)
        self.questions[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.update_data['title'], self.questions[0].title)
        self.assertEqual(self.update_data['text'], self.questions[0].text)
        self.assertEqual(
            self.update_data['course'], self.questions[0].course.pk)

    def test_update_question_asker(self):
        new_asker = GucianFactory()
        self.update_data['asker'] = new_asker.pk

        response = response = self.client.patch(
            path=self.detail_path, data=self.update_data)
        self.questions[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(new_asker.pk, self.questions[0].asker.pk)

    def test_update_question_created_at(self):
        self.update_data['created_at'] = datetime.datetime(2000, 5, 26)

        response = response = self.client.patch(
            path=self.detail_path, data=self.update_data)
        self.questions[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(
            self.update_data['created_at'], self.questions[0].created_at)

    def test_update_question_up_votes(self):
        self.update_data['up_votes'] = 1000

        response = response = self.client.patch(
            path=self.detail_path, data=self.update_data)
        self.questions[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(
            self.update_data['up_votes'], self.questions[0].up_votes)

    def test_update_question_down_votes(self):
        self.update_data['down_votes'] = 1000

        response = response = self.client.patch(
            path=self.detail_path, data=self.update_data)
        self.questions[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(
            self.update_data['down_votes'], self.questions[0].down_votes)


class QuestionVotingViewsTestSuite(BaseQuestionTestSuite):

    def setUp(self):
        super().setUp()
        self.up_vote_path = reverse(
            'question-up-vote', kwargs={'pk': self.questions[0].pk})
        self.down_vote_path = reverse(
            'question-down-vote', kwargs={'pk': self.questions[0].pk})

    def test_up_vote_non_existing_question(self):
        non_existing_path = reverse('question-up-vote', kwargs={'pk': 100})
        response = self.client.get(non_existing_path)

        self.assertEqual(404, response.status_code)

    def test_up_vote_question(self):
        old_up_votes_count = self.questions[0].up_votes
        response = self.client.get(self.up_vote_path)
        self.questions[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(old_up_votes_count + 1, self.questions[0].up_votes)

    def test_down_vote_non_existing_question(self):
        non_existing_path = reverse('question-down-vote', kwargs={'pk': 100})
        response = self.client.get(non_existing_path)

        self.assertEqual(404, response.status_code)

    def test_down_vote_question(self):
        old_down_votes_count = self.questions[0].down_votes
        response = self.client.get(self.down_vote_path)
        self.questions[0].refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertEqual(old_down_votes_count + 1,
                         self.questions[0].down_votes)
