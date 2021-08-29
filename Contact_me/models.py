from django.db import models

class Contact(models.Model):
    name    = models.CharField( 'Name' , max_length=30 , blank=True , null=True)
    email   = models.EmailField('Email' , blank=True , null=True )
    subject = models.CharField( 'Subject' , max_length=30 , blank=True , null=True)
    message = models.TextField( 'Mesmessage' , max_length=300 , blank=True , null=True)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")
    
    def __str__(self):
        return f"{self.name}"