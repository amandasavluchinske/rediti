def update_user_karma(user):
    karma_count = 0
    for post in user.posts.all():
        karma_count += post.vote_count
    for thread in user.threads.all():
        karma_count += thread.vote_count
    user.karma = karma_count
    user.save()