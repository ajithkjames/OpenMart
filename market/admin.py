# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from market.models import Category, Advertisement


class BaseModelMixinAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at')


admin.site.register(Category, BaseModelMixinAdmin)
admin.site.register(Advertisement, BaseModelMixinAdmin)