from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email


class CashierUser(CustomUser):

    def save(self, *args, **kwargs):
        if not self.is_staff:
            self.is_staff = True
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name_plural = 'کاربران مدیریت صندوق'

    # def get_profile_url(self):
    #     return 'managers/restaurants/'


class ClientUser(CustomUser):
    class Meta:
        proxy = True
        verbose_name_plural = 'کاربران معمولی'

    # def get_profile_url(self):
    #     return 'clients/profile/'  # Example URL
