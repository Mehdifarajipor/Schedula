from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extera_fields):
        if not email:
            raise ValueError("email is required!!!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extera_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extera_fields):
        extera_fields.setdefault('is_staff', True)
        extera_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extera_fields)