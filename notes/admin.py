from django.contrib import admin
from . import models
class Notesadmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(models.Notes,Notesadmin)
# Register your models here.
