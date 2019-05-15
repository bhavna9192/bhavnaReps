from django import forms
from .models import Student,loginModel,registerModel
from django.contrib.auth.forms import UserCreationForm

class NameForm(forms.Form):
    Description = forms.CharField(label='Description', max_length=100)

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ( 'name', 'age','last_name','email') 
       
    def clean_email(self):
        email = self.cleaned_data['email']
        if Student.objects.filter(email=email).count()>0:        
            raise forms.ValidationError('user with this email already exist')
        return email    


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')    	

class updateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ( 'name', 'age','last_name','email')  


class loginForm(forms.ModelForm):

    class Meta:
        model = loginModel
        fields = ( 'email', 'password')        

class registerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = registerModel         
        fields = ( 'name', 'email','age')




class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None




                      