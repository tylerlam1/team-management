from django.db import models
from django.core.validators import RegexValidator

from manager.utils.constants import MAX_EMAIL_LENGTH, MAX_NAME_LENGTH, MAX_PHONE_NUM_LENGTH

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+000000000'.")
email_regex = RegexValidator(regex=r'\w[\w\.-]*@\w[\w\.-]+\.\w+', message="Email must be entered in the format: 'tyler@hogwarts.edu.")

"""
Teammate model for storing information regarding teammates.
"""
class Teammate(models.Model):
    first_name = models.CharField(max_length=MAX_NAME_LENGTH)
    last_name = models.CharField(max_length=MAX_NAME_LENGTH)
    phone_number = models.CharField(validators=[phone_regex], max_length=MAX_PHONE_NUM_LENGTH)
    email = models.CharField(validators=[email_regex], max_length=MAX_EMAIL_LENGTH)
    is_admin = models.BooleanField(default=False)