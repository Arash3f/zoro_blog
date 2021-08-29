from Account import models
from django.contrib import admin

@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display  = ['__str__']

@admin.register(models.Skill)
class skillAdmin(admin.ModelAdmin):
    list_display  = ['title','amount']

@admin.register(models.Experience)
class experiencesAdmin(admin.ModelAdmin):
    list_display  = ['title' , 'Date']
    list_filter = ['Date']
  
@admin.register(models.Service)
class servicesAdmin(admin.ModelAdmin):
    list_display  = ['title' ]
    