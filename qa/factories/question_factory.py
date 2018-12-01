import factory
import random

from ..factories import CourseFactory
from ..models import Question

from users.factories import GucianFactory


class QuestionFactory(factory.DjangoModelFactory):
    """
    Question instances Generator.
    """
    class Meta:
        model = Question
    course = factory.SubFactory(CourseFactory)
    asker = factory.SubFactory(GucianFactory)

    title = factory.Faker('text')
    text = factory.Faker('text')
    up_votes = random.randint(1, 100)
    down_votes = random.randint(1, 100)
