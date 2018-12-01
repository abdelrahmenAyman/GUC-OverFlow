from django.test import TestCase

from qa.factories import AnswerFactory


class AnswerTestSuite(TestCase):

    def setUp(self):
        self.answer = AnswerFactory()

    def test_str_representation(self):
        self.assertEqual(self.answer.text, str(self.answer))

    def test_votes_representation(self):
        votes = self.answer.up_votes - self.answer.down_votes
        self.assertEqual(votes, self.answer.votes)

    def test_up_vote_on_answer(self):
        old_votes = self.answer.up_votes
        self.answer.up_vote()

        self.assertEqual(old_votes + 1, self.answer.up_votes)

    def test_down_vote_on_answer(self):
        old_votes = self.answer.down_votes
        self.answer.down_vote()

        self.assertEqual(old_votes + 1, self.answer.down_votes)
