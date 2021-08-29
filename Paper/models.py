from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from Account.models import User
from django.urls import reverse

class My_Papers(models.Model):
    title    = models.CharField( 'Title' , max_length=30 , blank=True , null=True)
    slug     = models.SlugField()
    summery  = RichTextField()
    body     = RichTextField()
    picture  = models.ImageField( 'Picture' , upload_to='paper/picture/' , blank=True , null=True ,help_text="555x471")
    tag      = TaggableManager()
    created_at  = models.DateTimeField( 'Created_at' , auto_now_add=True )
    updated_at  = models.DateTimeField( 'Updated_at' , auto_now=True)
    view     = models.IntegerField('Views'  ,default=0 ,blank=True ,null=True)
    author   = models.ForeignKey(User , on_delete=models.CASCADE , related_name='paper')
    publish  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Paper")
        verbose_name_plural = ("Papers")
    
    def format_date(self):
        return self.created_at.strftime("%Y/%m/%d")
        
    def get_absolute_url(self):
        return reverse('paper:paper_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])
    
    def view_plus(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        view_list =[]
        for i in self.paper_view.all():
            view_list.append(i.ip)
        if ip not in view_list:
            paper = My_Papers.objects.get(id=self.id)
            add_view = View.objects.create(ip=ip , paper=paper)
            add_view.save()
            self.view +=  1
            self.save()
    
    def __str__(self):
        return f"{self.title}"
    
    def tags_name(self):
        return (" ".join(i.name for i in self.tag.all()))
    
    def tags_name_for_admin(self):
        return (", ".join(i.name for i in self.tag.all()))

    tags_name_for_admin.short_description = "tags"
    
class View(models.Model):
    ip = models.CharField('ip' ,max_length=30 ,blank=True , null=True )
    paper = models.ForeignKey('My_Papers' , on_delete=models.CASCADE , related_name='paper_view')
    