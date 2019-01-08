def increase_vote_count(target):
    target.vote_count += 1
    target.save()

def decrease_vote_count(target):
    target.vote_count -= 1
    target.save()