import factory
import random

from ..models import Answer
from ..factories import QuestionFactory

from users.factories import GucianFactory


class AnswerFactory(factory.DjangoModelFactory):
    """Answer instances Generator."""
    class Meta:
        model = Answer

    question = factory.SubFactory(QuestionFactory)
    answerer = factory.SubFactory(GucianFactory)

    text = factory.Faker('text')
    up_votes = random.randint(1, 100)
    down_votes = random.randint(1, 100)
