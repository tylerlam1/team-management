from django.db import models

from manager.utils.constants import MAX_EMAIL_LENGTH, MAX_NAME_LENGTH, MAX_PHONE_NUM_LENGTH

# Create your models here.
class Teammate(models.Model):
    first_name = models.CharField(max_length=MAX_NAME_LENGTH)
    last_name = models.CharField(max_length=MAX_NAME_LENGTH)
    phone_number = models.CharField(max_length=MAX_PHONE_NUM_LENGTH)
    email = models.CharField(max_length=MAX_EMAIL_LENGTH)
    is_admin = models.BooleanField(default=False)