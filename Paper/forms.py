from Comment.models import Comment
from django import forms

class Comment_From(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('body',)
        widgets = {
            'body'   : forms.Textarea(attrs={'class':"form-control mb-10" , "type":"text" , "name":"message" , "placeholder":"Comment"}),
        }
        labels = {
           'body'    :''}