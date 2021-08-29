from django.db import models
from Paper.models import My_Papers
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_comment')
    Date = models.DateField( 'Date' , auto_now_add=True ,  blank=True , null=True)
    body = models.TextField( 'Body', blank=True , null=True)
    paper = models.ForeignKey(My_Papers , on_delete=models.CASCADE , related_name='paper_comment')

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return f"{self.user}"

    def format_date(self):
        return self.Date.strftime("%Y/%m/%d")