import factory

from ..models import Course


class CourseFactory(factory.DjangoModelFactory):
    """
    Course Model instances Generator.
    """
    class Meta:
        model = Course

    name = factory.Faker('text')
    code = factory.Faker('text')
