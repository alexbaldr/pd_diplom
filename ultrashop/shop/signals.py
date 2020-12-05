from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver, Signal
from registration.models import User

new_order = Signal(providing_args=['user_id'],)


@receiver(new_order)
def new_order_reciver(user_id, **kwargs):
    user = User.objects.get(id=user_id)
    message = EmailMultiAlternatives(
        # title:
        f"Обновление статуса заказа",
        # message:
        'Заказ сформирован',
        # from:
        settings.DEFAULT_FROM_EMAIL,
        # to:
        [user.email]
    )
    message.send()

