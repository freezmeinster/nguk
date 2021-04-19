# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
