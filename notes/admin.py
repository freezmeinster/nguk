# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'location']
