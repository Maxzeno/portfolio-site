from django.db.models.signals import post_save
from django.dispatch import receiver
from main import models
from django.core.mail import send_mail

from decouple import config


@receiver(post_save, sender=models.ContactModel)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            f"{instance.subject} - {instance.email} - {instance.fullname}",
            f"Email From {instance.fullname} - {instance.email} \n{instance.message}",
            config('EMAIL_HOST_USER'),
            [config('ADMIN_EMAIL')],
            fail_silently=False,
        )
