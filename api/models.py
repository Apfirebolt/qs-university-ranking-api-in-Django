from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class MyUserManager(BaseUserManager):
  def create_superuser(self, email, password):
    user = self.model(email=email)
    user.set_password(password)
    user.is_superuser = True
    user.is_active = True
    user.is_staff = True
    user.save(using=self._db)
    return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email", unique=True, max_length=255, blank=True, null=True)
    username = models.CharField("User Name", unique=True, max_length=255, blank=True, null=True)
    is_active = models.BooleanField('Active', default=True, blank=True, null=True)
    is_staff = models.BooleanField('Staff', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
      return self.email


class University(models.Model):
  name = models.CharField('University Name', max_length=200)
  country = models.CharField('Country', max_length=50)
  location = models.CharField('Location', max_length=100)
  name = models.CharField('University Name', max_length=200)
  rank = models.IntegerField('University Rank')
  ar_score = models.FloatField('University AR Score')
  ar_rank = models.CharField('University AR Rank', max_length=10)

  def __str__(self):
    return str(self.name) + ' - ' + str(self.country)

  class Meta:
    verbose_name_plural = "Universities"