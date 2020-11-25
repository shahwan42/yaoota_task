from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    """
    User model manager where username is the unique identifiers
    for authentication.
    """

    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given username and password.
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given username and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, password, **extra_fields)


class User(TimeStampedModel, AbstractUser):
    # Removed from base class
    first_name = None
    last_name = None

    # required
    name = models.CharField(max_length=255, blank=True)
    mobile = PhoneNumberField(unique=True, blank=True)

    objects = UserManager()

    def __str__(self) -> str:
        return self.get_short_name()

    def __repr__(self) -> str:
        if self.name:
            return f"<User {self.id}: {str(self)}>"
        return f"<User {self.id}>"

    def get_full_name(self) -> str:
        return self.name

    def get_short_name(self) -> str:
        name_list = self.name.split(" ")
        if len(name_list) > 0:
            return name_list[0]
        return ""
