from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True,  # Allow blank, but we'll require it in serializer
        help_text='Optional unique username (can be used for profile URL later)',
    )
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'      # Login with email
    REQUIRED_FIELDS = []          # No extra fields required for createsuperuser

    objects = CustomUserManager()

    def __str__(self):
        return self.username or self.email