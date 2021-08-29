from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.contrib.auth.models import User

class registerform(forms.ModelForm):
    class Meta:
        model = User
        fields =('username', 'first_name', 'last_name', 'email' ,'password')
        widgets = {
            'username'    :     forms.TextInput(attrs={'class':"input--style-4" , "type":"text"  , "name":"username" }),
            'first_name'  :     forms.TextInput(attrs={'class':"input--style-4" , "type":"text" , "name":"first_name"}),
            'last_name'   :     forms.TextInput(attrs={'class':"input--style-4" , "type":"text", "name":"last_name"  }),
            'email'       :     forms.EmailInput (attrs={'class': "input--style-4" , "type":"email" , "name":"email"   }),
            'password'    :     forms.PasswordInput (attrs={'class': "input--style-4" , "type":"password" , "name":"password"   }),
        }
    def clean(self):
        
        cd = self.cleaned_data
        username = cd.get('username')
        first_name= cd.get('first_name')
        last_name= cd.get('last_name')
        password = cd.get('password')
        email = cd.get('email')
        if first_name=="" :
            raise ValidationError("Please Enter first name ")
        elif last_name=="":
            raise ValidationError("Please Enter last name ")
        elif email=="":
            raise ValidationError("Please Enter email")
        elif User.objects.filter(Q(username=username)|Q(email=email)):
            raise ValidationError("Username or Email already is exist")
        return cd


 