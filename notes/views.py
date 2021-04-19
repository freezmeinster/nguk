# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from models import Note

def landing(request):
    return render(request, "landing.html")

def list_note(request):
    data = list()
    for note in Note.objects.all():
        data.append({
            "id": note.id,
            "title": note.title,
            "location": note.location,
        })
    return JsonResponse(data, safe=False)
