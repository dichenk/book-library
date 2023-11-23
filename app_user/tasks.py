from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email(user_email):
    send_mail(
        'Добро пожаловать!',
        'Мы рады видеть вас в нашей библиотеке!',
        'o02380897@gmail.com',
        [user_email],
        fail_silently=False,
    )
