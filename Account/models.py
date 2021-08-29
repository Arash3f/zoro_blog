from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class User(models.Model):
    user            = models.OneToOneField( User , related_name='user',  on_delete=models.CASCADE)
    picture_main    = models.ImageField  ( ' picture for portfolio' , upload_to='User_Pictures/' , blank=True , null=True ,help_text="485x600")
    picture_blog    = models.ImageField  (  'picture for blog' , upload_to='User_Pictures/' , blank=True , null=True ,help_text="120x120")
    summery         = RichTextField()
    about           = RichTextField()
    end_about_me    = RichTextField()
    job             = models.CharField   ( 'Job'       , max_length=30 , blank=True , null=True)
    date_of_birth   = models.DateField   ( 'Date of birth' , blank=True , null=True)
    phone           = models.CharField   ( 'Phone'     , max_length=11 , blank=True , null=True)
    Location        = models.CharField   ( 'Location'  , max_length=30 , blank=True , null=True)
    github          = models.CharField   ( 'Github'    , max_length=100 , blank=True , null=True)
    skype           = models.CharField   ( 'Skype'  , max_length=100 , blank=True , null=True)
    twitter         = models.CharField   ( 'Twitter'   , max_length=100 , blank=True , null=True)
    instagram       = models.CharField   ( 'Instagram' , max_length=100 , blank=True , null=True)
    total_project   = models.IntegerField('Total project'    , default=0 , blank=True , null=True)
    total_volunteers= models.IntegerField('Total volunteers' , default=0 , blank=True , null=True)
    total_donation  = models.IntegerField('Total donation'   , default=0 , blank=True , null=True)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Informations")

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    title  = models.CharField   ( 'Title'  , max_length=30 , blank=True , null=True)
    amount = models.IntegerField( 'Amount' , default=0 , blank=True , null=True)

    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")
    
    def __str__(self):
        return self.title
    
class Experience(models.Model):
    title     = models.CharField( 'Title' , max_length=30 , blank=True , null=True)
    about     = models.TextField( 'About',max_length=100 , blank=True  , null=True )
    Date      = models.DateField( 'Date' , blank=True , null=True)

    class Meta:
        verbose_name = ("Experience")
        verbose_name_plural = ("Experiences")
    
    def __str__(self):
        return self.title
    
    def format_date(self):
        return self.Date.strftime("%Y/%m/%d")
    
class Service(models.Model):
    title     = models.CharField( 'Title' , max_length=30 , blank=True , null=True)
    about     = RichTextField()

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")
    
    def __str__(self):
        return self.title