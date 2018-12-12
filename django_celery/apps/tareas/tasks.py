from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django_celery import settings
import time

@shared_task
def send_emails_users():
	asunto= 'Mensaje de prueba'
	mensaje= 'Bienvenido esto es un mensaje de prueba celery'
	users = User.objects.all()

	for user in users:
		send_mail(asunto,mensaje,settings.EMAIL_HOST_USER,[user.email],fail_silently=False)
	return '{} se envio correo correctamente'.format(user)