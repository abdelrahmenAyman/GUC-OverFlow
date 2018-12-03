from django.test import TestCase

from qa.factories import QuestionFactory


class QuestionTestSuite(TestCase):

    def setUp(self):
        self.question = QuestionFactory()

    def test_str_representation(self):
        self.assertEqual(self.question.title, str(self.question))

    def test_votes_representation(self):
        votes = self.question.up_votes - self.question.down_votes
        self.assertEqual(votes, self.question.votes)

    def test_up_vote_on_question(self):
        old_votes = self.question.up_votes
        self.question.up_vote()

        self.assertEqual(old_votes + 1, self.question.up_votes)

    def test_down_vote_on_question(self):
        old_votes = self.question.down_votes
        self.question.down_vote()

        self.assertEqual(old_votes + 1, self.question.down_votes)
