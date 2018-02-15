# coding=utf-8
from django.contrib.gis.db import models


class LocationType(models.Model):

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u'%s' % self.name
