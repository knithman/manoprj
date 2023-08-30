from django.contrib import admin

from .models import Kompiuteris, Stacionarus, Nesiojamas
# Register your models here.

admin.site.register(Kompiuteris)
admin.site.register(Stacionarus)
admin.site.register(Nesiojamas)
