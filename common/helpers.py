from subs.models import Post, Thread
from .models import VotePost, VoteThread
from users.helpers import update_user_karma

def return_thread_or_post(target_type, target_id, user):
    if target_type == 'post':
        return Post.objects.get(id=target_id)
    if target_type == 'thread':
        return Thread.objects.get(id=target_id)

def return_votethread_or_votepost(target_type, target, user):
    if target_type == 'post':
        return VotePost.objects.get_or_create(post=target, user=user)
    if target_type == 'thread':
        return VoteThread.objects.get_or_create(thread=target, user=user)

def modify_vote_count(vote, target):
    if vote.count == 1:
        vote.count = 0
        vote.save()
        target.vote_count -= 1
        target.save()
        return
    vote.count = 1
    vote.save()
    target.vote_count += 1
    target.save()
    return

def modify_karma(target_type, target_id, user):
    target = return_thread_or_post(target_type, target_id, user)
    vote, created = return_votethread_or_votepost(target_type, target, user)
    modify_vote_count(vote, target)
    update_user_karma(target.author)