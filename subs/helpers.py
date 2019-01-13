from .models import Subscription, Subrediti


def subscribe_or_unsubscribe(sub_id, user):
    sub = Subrediti.objects.get(id=sub_id)
    subs, created = Subscription.objects.get_or_create(subrediti=sub, user=user)
    if subs.subscribed == False:
        subs.subscribed = True
        subs.save()
        return
    subs.subscribed = False
    subs.save()
    return