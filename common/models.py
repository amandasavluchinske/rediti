from django.db import models
from django.utils.translation import ugettext_lazy as _


class IndexedTimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VoteThread(models.Model):
    user = models.ForeignKey('users.user', related_name='votes_threads', on_delete=models.CASCADE)
    thread = models.ForeignKey('subs.Thread', related_name='votes_threads', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = (('user', 'thread'))


class VotePost(models.Model):
    user = models.ForeignKey('users.user', related_name='votes_posts', on_delete=models.CASCADE)
    post = models.ForeignKey('subs.Post', related_name='votes_posts', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = (('user', 'post'))