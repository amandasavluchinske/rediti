from subs.models import Post, Thread
from .models import VotePost, VoteThread
from users.helpers import update_user_karma

def return_thread_or_post(target_type, target_id, user, vote_type):
    if vote_type == 'upvote':
        vote = 1
    if vote_type == 'downvote':
        vote = -1
    if target_type == 'post':
        VotePost.objects.create(post=target_id, user=user, vote=vote)
        return Post.objects.get(id=target_id)
    if target_type == 'thread':
        VoteThread.objects.create(post=target_id, user=user, vote=vote)
        return Thread.objects.get(id=target_id)

def check_for_repeated_vote(target_type, target_id, vote_type):
    if target_type == 'post':
        vote = VoteThread.objects.get(id=target_id)
    if target_type == 'thread':
        vote = VotePost.objects.get(id=target_id)
    if vote_type == 'upvote' and vote.count == 1:
        return True
    if vote_type == 'downvote' and vote.count == -1:
        return True
    return False


def modify_post_karma(target_type, target_id, user, vote_type):
    if check_for_repeated_vote(target_type, target_id, vote_type):
        return
    target = return_thread_or_post(target_type, target_id, user, vote_type)
    if vote_type == 'upvote':
        target.vote_count +=1
    if vote_type == 'downvote':
        target.vote_count -= 1
    target.save()
    update_user_karma(target.author)