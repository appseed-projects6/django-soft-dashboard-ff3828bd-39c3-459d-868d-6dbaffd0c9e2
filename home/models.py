# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Quality_Of_Service(models.Model):

    #__Quality_Of_Service_FIELDS__
    node:limit:req = models.CharField(max_length=255, null=True, blank=True)
    pod:limit:req = models.CharField(max_length=255, null=True, blank=True)

    #__Quality_Of_Service_FIELDS__END

    class Meta:
        verbose_name        = _("Quality_Of_Service")
        verbose_name_plural = _("Quality_Of_Service")


class (models.Model):

    #___FIELDS__

    #___FIELDS__END

    class Meta:
        verbose_name        = _("")
        verbose_name_plural = _("")



#__MODELS__END
