from django import forms
from django.contrib.auth import get_user_model
from django.db.models.functions import Length


User = get_user_model()

class LoginForm(forms.Form):
    username= forms.CharField(required=True)
    password= forms.CharField(widget=forms.PasswordInput, required=True)



class RegisterForm(forms.Form):
    username                = forms.CharField(label="username", required=True)
    email                   = forms.EmailField(label="email address", required=True)
    password                = forms.CharField(widget=forms.PasswordInput, required=True)
    password2               = forms.CharField(label='Confirm Password' , widget=forms.PasswordInput, required=True)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username



#    def clean_mobile(self):
#        mobile = self.cleaned_data.get('mobile')
#        if len(mobile) is not 10:
#            raise forms.ValidationError("Mobile Number is wrong")
#        return mobile

    #def clean_email(self):
    #    email = self.cleaned_data.get('email')
    #    qs = User.objects.filter(email=email)
    #    if qs.exists():
    #        raise forms.ValidationError("email is taken")
    #    return email

    def clean(self):
         data = self.cleaned_data
         password=self.cleaned_data.get('password')
         password2=self.cleaned_data.get('password2')
         if password2 != password:
             raise forms.ValidationError("Passwords must match")
         return data
