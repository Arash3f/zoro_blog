from django.shortcuts import render 

def handler404(request, exception):
    template_name="404.html"
    return render(request,template_name)