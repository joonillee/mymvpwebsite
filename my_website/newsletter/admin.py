# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import SignUp
# importing SignUp model into admin by .models since inside the app already
from .forms import SignUpForm
# importing SigUpFrom from forms.py

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm
    #class Meta:
        #model = SignUp


admin.site.register(SignUp, SignUpAdmin)
