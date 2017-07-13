# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
#from pip._vendor.appdirs import unicode


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Test(models.Model):
    name = models.TextField(max_length=250)
    password = models.TextField(max_length=250)
    sex = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()


class UploadFileModel(models.Model):
    title = models.TextField(default='')
    author =models.CharField(default='',max_length=50)
    file = models.FileField(null=True)