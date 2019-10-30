from django.contrib.auth.models import User
from django.db import models
# from __future__ import unicode_literals


class Token (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    # def __unicode__(self):
    #     return "{}-token".format(self.user)


class Expense(models.Model):
    text = models.TextField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __unicode__(self):
    #     return "{}-{}".format(self.date, self.amount)


class Income(models.Model):
    text = models.TextField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)