from django.db import models
from common.models import IndexedTimeStampedModel

class Subrediti(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    creator = models.ForeignKey('users.User', related_name="subreditis", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Thread(IndexedTimeStampedModel):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('users.User', related_name="threads", on_delete=models.CASCADE)
    subrediti = models.ForeignKey('Subrediti', related_name="threads", on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Post(IndexedTimeStampedModel):
    content = models.TextField()
    author = models.ForeignKey('users.User', related_name="posts", on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', related_name="posts", on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return ("{} - {} - {}").format(self.id, self.thread, self.author)


class Subscription(models.Model):
    subrediti = models.ForeignKey('Subrediti', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = [('subrediti', 'user')]

    def __str__(self):
        return ("{} - {}").format(self.subrediti, self.user)