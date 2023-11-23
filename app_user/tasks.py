from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import shared_task


@shared_task
def send_welcome_email(user_email):
    html_content = render_to_string('emails/welcome.html', {'email': user_email})
    text_content = strip_tags(html_content)

    send_mail(
        'Добро пожаловать!',
        text_content,
        'o02380897@gmail.com',
        [user_email],
        html_message=html_content,
        fail_silently=False,
    )
