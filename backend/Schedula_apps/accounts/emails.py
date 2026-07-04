from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator


def send_reset_email(user, request):

    token = PasswordResetTokenGenerator().make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    protocol = "https" if request.is_secure() else "http"
    domain = request.get_host()
    reset_url = f"{protocol}://{domain}/api/accounts/password_reset/{uid}/{token}"

    context = {
        'user': user,
        'uid': uid,
        'token': token,
        'protocol': protocol,
        'domain': domain,
        'reset_url': reset_url,

    }

    subject = render_to_string("accounts/password_reset_subject.txt", context)
    body_txt = render_to_string("accounts/password_reset_email.txt", context)
    body_html = render_to_string("accounts/password_reset_email.html", context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=body_txt,
        to=[user.email],
    )

    email.attach_alternative(body_html, "text/html")
    email.send(fail_silently=False)

