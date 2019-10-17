from django.db.models.signals import post_save
from django.dispatch import receiver
from mainapp.models import InputImages
from mainapp.tasks import save_image_to_models


@receiver(post_save, sender=InputImages)
def save_image_to_model(sender, **kwargs):
    save_image_to_models.delay()
