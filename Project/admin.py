from Project import models
from django.contrib import admin

@admin.register(models.Project)
class Project(admin.ModelAdmin):
    list_display  = ['title']
    prepopulated_fields = {'slug': ('title',), }