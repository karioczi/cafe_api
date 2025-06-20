from django.core.mail import send_mail
from django.conf import settings

def send_password_reset_email(user, uid, token):
    reset_link = f'https://yourfrontend.com/reset-password/?uid={uid}&token={token}'
    subject = 'Password Reset Request'
    message = f'Hello {user.username}, \n\nUse this link to reset your password:\n{reset_link}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])