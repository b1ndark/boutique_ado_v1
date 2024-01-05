from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderlineItem


@receiver(post_save, sender=OrderlineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderlineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    print('fsdfsdfs')
    instance.order.update_total()
