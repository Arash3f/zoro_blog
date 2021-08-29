from django.contrib import admin
from Comment import models

@admin.register(models.Comment)
class Comment(admin.ModelAdmin):
    list_display  = ['__str__','paper']
