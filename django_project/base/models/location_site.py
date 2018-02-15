# coding=utf-8
from django.contrib.gis.db import models


class Location(models.Model):

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    polygon = models.PolygonField(
        null=True,
        blank=True,
        srid=4326
    )

    point = models.PointField(
        null=True,
        blank=True,
        srid=4326
    )

    line = models.LineStringField(
        null=True,
        blank=True,
        srid=4326
    )

    def __unicode__(self):
        return u'%s' % self.name
