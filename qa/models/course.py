from django.db import models


class Course(models.Model):
    """
    Represents a course that is taught under GUC.
    """
    name = models.CharField(max_length=350)
    code = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.code
