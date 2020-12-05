from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver, Signal
# from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework.authtoken.models import Token


new_user_registered = Signal(
    providing_args=['user_id'],
)


@receiver(new_user_registered)
def get_token(user_id=None, **kwargs):
    token = Token.objects.create(user=user_id)
    message = EmailMultiAlternatives(
        # title:
        f"Password Reset Token for {token.user.email}",
        # message:
        token.key,
        # from:
        settings.DEFAULT_FROM_EMAIL,
        # to:
        [token.user.email]
    )
    message.send()
