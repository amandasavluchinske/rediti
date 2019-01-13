from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class IndexedTimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VoteAbstractModel(models.Model):
    user = models.ForeignKey('users.user', on_delete=models.CASCADE)
    count = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ])

    class Meta:
        abstract = True


class VoteThread(VoteAbstractModel):
    thread = models.ForeignKey('subs.Thread', related_name='votes_threads', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'thread'))


class VotePost(VoteAbstractModel):
    post = models.ForeignKey('subs.Post', related_name='votes_posts', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'post'))