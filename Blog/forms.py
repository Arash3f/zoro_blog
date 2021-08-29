from django import forms

class SearchFrom(forms.Form):
    query = forms.CharField(label=False)
    query.widget.attrs.update({"type":"text" ,"class":"form-control" ,"placeholder":"Search Posts"})
