from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from ultrashop.celery import app
from ultrashop.settings import DEFAULT_FROM_EMAIL


@app.task
def send_token_task(user_id=None, **kwargs):
    token = Token.objects.create(user=user_id)
    send_mail(
        # title:
        subject=f"Password Reset Token for {token.user.email}",
        # message:
        message=token.key,
        # from:
        from_email=DEFAULT_FROM_EMAIL,
        # to:
        recipient_list=[token.user.email],
        fail_silently=True,
    )
