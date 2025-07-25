from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role='CUSTOMER', **extra_fields):  # ✅ FIXED CASE
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email,
            password,
            role='ADMIN', 
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
