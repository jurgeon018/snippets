from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser, AbstractUser, User
    PermissionsMixin
)
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
    def create_user(self, username,  password, email=None, phone_number=None, date_of_birth=None):
        # if not email:
        #     raise ValueError('Users must have an email address')
        if not username:
            raise ValueError(_('Users must have an username'))
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  password, email=None, phone_number=None, date_of_birth=None):
        print('ssssss')
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username      = models.CharField(verbose_name=_('username'), max_length=255, unique=True)
    email         = models.EmailField(verbose_name='email address', max_length=255,  blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    first_name    = models.CharField(max_length=30, blank=True)
    last_name     = models.CharField(max_length=150, blank=True)
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    date_joined   = models.DateTimeField(default=timezone.now)
    objects       = CustomUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
    def __str__(self):
        return f'{self.email}, {self.username}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_staff



class Profile(models.Model):
    user       = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio        = models.TextField(max_length=500, blank=True)
    location   = models.CharField(max_length=30, blank=True)
    avatar     = models.ImageField(blank=True, null=True, upload_to='pics/')


@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()