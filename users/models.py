from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from core.models import SoftDeleteModel
from users.managers import UserManager

class User(SoftDeleteModel, AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        CUSTOMER = 'CUSTOMER', 'Customer'

    email = models.EmailField(unique=True, db_index=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CUSTOMER)
    phone_number = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['name']
