from django.shortcuts import render
from django.db.utils import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms


# Create your views here.
class CustomSignUpForm(UserCreationForm):
    ''' creating a user form from the django user model
        add an email field with regex fuction

    '''

    #creating a regex for the username feild for email 
    email_validator = RegexValidator(
        regex=r'^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$',
        message='Enter a valid email address.',
        code='invalid_email'
        )
    email = forms.CharField(
        max_length = 30,
        required =True,
        #help_text = 'Enter a valid email adress',
        validators = [email_validator]
        )
    
    class Meta:
        model = User
        fields = ('email', 'first_name','password1', 'password2')

    def save(self, commit=True):
        ''' use the email as the username, 
        therefore override the save() method
        '''
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user


class SignUpView(generic.CreateView):
    ''' Creating a sign up view from the generic class views 
        this Class is instantiated as a view in the url.py 

        Handle Integretory error signup errors where user/email already exsists

    '''
    #setting up the signup view 
    form_class = CustomSignUpForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            form.add_error('email', 'This email is already in use')
            return self.form_invalid(form)
        


def user_login(request):
    
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    '''Verify user input password and username 
        handle handles errors where user doesn't exsist
    '''
    email_input = request.POST['email']
    password_input = request.POST['password']

    
    user = authenticate(request, username=email_input, password=password_input)
    

    if user is None:

        if User.objects.filter(username=email_input).exists():
            error_message = "Email does not exist.."
        else:
            error_message =  "Password incorrect"

        print(error_message)
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        print(f"signed in user:{user.get_username()}")
        return HttpResponseRedirect(reverse('dashboard:discover'))
   

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard:landing'))
