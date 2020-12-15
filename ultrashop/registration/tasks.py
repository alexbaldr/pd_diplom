from celery import shared_task
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.conf import settings
from ultrashop.celery import app


@app.task
def send_token_task(user_id=None, **kwargs):
    token = Token.objects.create(user=user_id)
    send_mail(
        # title:
        subject=f"Password Reset Token for {token.user.email}",
        # message:
        message=token.key,
        # from:
        from_email=settings.DEFAULT_FROM_EMAIL,
        # to:
        recipient_list=[token.user.email],
        fail_silently=False,
    )
