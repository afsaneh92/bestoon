from django.contrib import admin

from . import models

admin.site.register(models.Expense)
admin.site.register(models.Income)
admin.site.register(models.Token)