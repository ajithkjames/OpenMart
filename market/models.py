# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import User


class ModelManager(models.Manager):
    def get_queryset(self, fetch_all=False):
        return super(ModelManager, self).get_queryset() if fetch_all \
            else super(ModelManager, self).get_queryset().all()


class DateMixin(models.Model):

    objects = ModelManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            abstract = True


class Category(DateMixin):
    """Category model"""

    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):         
            return self.name


class Advertisement(DateMixin):
    """Advertisement model"""

    author = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    views = models.PositiveIntegerField(null=True, blank=True, default=0)
    image = models.ImageField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
		return u'%s - %s' % (self.title, self.author)