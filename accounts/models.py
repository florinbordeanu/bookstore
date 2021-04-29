from django.db import models
from django.db.models import OneToOneField
from django.contrib.auth.models import User

genders = (
    ('M', 'masculine'),
    ('F', 'feminine')
)


class UserProfile(models.Model):

    user = OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    gender = models. CharField(choices=genders, max_length=15, null=True, blank=True)
    accepted_terms = models.BooleanField(default=False)
