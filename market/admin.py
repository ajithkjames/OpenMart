# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from market.models import Category, Advertisement


admin.site.register(Category)
admin.site.register(Advertisement)