from django.db import models
from django.utils.translation import ugettext_lazy as _


class IndexedTimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
