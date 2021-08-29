from django.contrib import admin
from Contact_me import models

@admin.register(models.Contact)
class Contact(admin.ModelAdmin):
    list_display  = ['name' ,'email']