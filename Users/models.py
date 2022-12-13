from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, required=True)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email']

    first_name = models.CharField(max_length=100, required=True)
    last_name = models.CharField(max_length=100, required=True)

    is_staff = models.BooleanField(
        default = False,
        help_text = """Designates whether the user can log into this admin site.""",
    )
    is_active = models.BooleanField(
        default = True,
        help_text =
            """Designates whether this user should be treated as active.
            Unselect this instead of deleting accounts."""
        ,
    )

    objects = UserManager()