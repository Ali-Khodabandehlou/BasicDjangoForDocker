from django.db import models


# base model for apps
class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_on']

    # todo: add loggable traits

