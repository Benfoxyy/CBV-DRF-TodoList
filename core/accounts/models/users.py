from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import ugettext as _

class UserManager(BaseUserManager):
    def create_user(self,email,password,**extera):
        if not email:
            raise ValueError(_('Please enter an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extera)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extera):
        extera.setdefault('is_staff',True)
        extera.setdefault('is_superuser',True)
        extera.setdefault('is_verified',True)
        if extera.get('is_staff') is not True:
            raise ValueError(_('is_staff must be True'))
        if extera.get('is_superuser') is not True:
            raise ValueError(_('is_superuser must be True'))
        return self.create_user(email,password,**extera)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email