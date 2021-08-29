from django.contrib import admin
from Paper import models

@admin.register(models.My_Papers)
class My_Papers(admin.ModelAdmin):
    list_display  = ['__str__','tags_name_for_admin']
    list_filter = ['tag']
    prepopulated_fields = {"slug": ("title",)}   