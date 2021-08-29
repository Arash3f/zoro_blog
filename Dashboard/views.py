

from django.shortcuts import render , get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from Dashboard import forms
from Comment.models import Comment

class register(CreateView):
    form_class = forms.registerform
    template_name="registration/register.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active=True
        user.is_staff=True
        user.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return '/portfolio'

class dashboard(LoginRequiredMixin,View):
    template_name="Dashboard/dashboard.html"
    login_url = '/account/login/'
    
    def get(self, request):
        return render(request,self.template_name)

    def post(self, request):
        
        first_name=request.POST.get('name')
        lastname=request.POST.get('last_name')
        password=request.POST.get('password')
        re_password=request.POST.get('re_password')
        email=request.POST.get('email')

        if first_name=="" or lastname=="" or password=="" or re_password=="" or email=="" or password!=re_password:
            return render(request,"404.html")

        try:
            up = get_object_or_404(User,username=request.user.username)
            up.first_name=first_name
            up.last_name=lastname
            up.password=make_password(password)
            up.email=email
            up.save()
        except:
            return render(request,"404.html")

        return render(request,self.template_name)
            
class comments(LoginRequiredMixin , ListView):
    login_url = '/account/login/'
    template_name="Dashboard/comments.html"
    model = Comment