from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title   = models.CharField( 'Title' , max_length=30 , blank=True , null=True)
    slug    = models.SlugField()
    summery = models.CharField( 'Summery' , max_length=150 , blank=True , null=True)
    body    = RichTextField()

    class Meta:
        unique_together = ['slug', 'title']
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")
    
    def __str__(self):
        return f"{self.title}"

    
    
    
    
    