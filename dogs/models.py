from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import User
# Create your models here.

class Dog(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    owner = models.ForeignKey(User, related_name='dog_owner')
    birthday = models.DateField(_('Date of birth'), blank=True, null=True)
    
    def __str__(self):
        return self.name
