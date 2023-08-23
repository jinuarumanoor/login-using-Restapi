from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class AccountManager(BaseUserManager):
    
    def create_user(self, username, email, phone_number, password=None):
        if not email:
            raise ValueError('User should have an email address ')

        if not username:
            raise ValueError('User must have an username') 

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, phone_number):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            phone_number=phone_number,
        )

        user.is_admin = True 
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user 


class Account(AbstractBaseUser):
    
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=75, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
