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
  fsr_score = models.CharField('University FSR Score', max_length=10)
  fsr_rank = models.CharField('University FSR Rank', max_length=10)
  cpf_score = models.CharField('University CPF Score', max_length=10)
  cpf_rank = models.CharField('University CPF Rank', max_length=10)
  ifr_score = models.CharField('University IFR Score', max_length=10)
  ifr_rank = models.CharField('University IFR Rank', max_length=10)
  isr_score = models.CharField('University ISR Score', max_length=10)
  isr_rank = models.CharField('University ISR Rank', max_length=10)
  irn_score = models.CharField('University IRN Score', max_length=10)
  irn_rank = models.CharField('University IRN Rank', max_length=10)
  ger_score = models.CharField('University GER Score', max_length=10)
  ger_rank = models.CharField('University GER Rank', max_length=10)
  score_sealed = models.CharField('University Score Sealed', max_length=10)

  def __str__(self):
    return str(self.name) + ' - ' + str(self.country)

  class Meta:
    verbose_name_plural = "Universities"