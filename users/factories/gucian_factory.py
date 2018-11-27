import factory
import factory.fuzzy
import random
import datetime

from ..models import Gucian
from ..factories import UserFactory


class GucianFactory(factory.DjangoModelFactory):
    """Author: Abdelrahmen Ayman"""

    class Meta:
        model = Gucian

    user = factory.SubFactory(UserFactory)

    guc_email = factory.Faker('email')
    backup_email = factory.Faker('email')
    dash_number = random.randint(1, 999)
    major = factory.Faker('job')
    bio = factory.Faker('text')
    reputation = random.randint(1, 400)
    birthdate = factory.fuzzy.FuzzyDate(
        start_date=datetime.date(1950, 1, 1),
        end_date=datetime.date.today() - datetime.timedelta(days=20 * 365),
    )
