from django.contrib import messages
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out


@receiver(user_logged_out)
def user_logged_out_message(request, **kwargs):
    messages.add_message(request, messages.INFO, 'Wylogowanie zakończyło się sukcesem. '
                                                 'Poniżej możesz zalogować się ponownie.')
