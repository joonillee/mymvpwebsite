from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email'] #these are the field that are showing up on admin ->singups->
        ### exclude = ['full_name'] not recommended but can use becasue 
        ### if you want to add something, this is not the best way  

    def clean_email(self): #form email field validation
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        donamin, extension = provider.split(".")
        # if not domain == 'USC':
        #     raise forms.ValidationError("Please make sure you use your USC email.")
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address")
        return email 

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # you can write validation error here
        return full_name