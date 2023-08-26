from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    # ...

    class User(AbstractBaseUser, PermissionsMixin):
        # ...

        # Define unique related names for groups and user_permissions fields
        # to avoid clashes with the built-in auth.User model
        groups = models.ManyToManyField(
            "auth.Group",
            related_name="user_custom_set",  # Use a distinct related name
            blank=True,
            verbose_name="groups",
            help_text="The groups this user belongs to.",
        )
        user_permissions = models.ManyToManyField(
            "auth.Permission",
            related_name="user_custom_set",  # Use a distinct related name
            blank=True,
            verbose_name="user permissions",
            help_text="Specific permissions for this user.",
        )

        # ...
