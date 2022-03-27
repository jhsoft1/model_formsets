from django.db import models


# https://www.youtube.com/watch?v=FnZgy-y6hGA A Quick Intro to Model Formsets in Django
# Pretty Printed
class Example(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
