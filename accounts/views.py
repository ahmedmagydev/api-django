from django.shortcuts import render , redirect
from django.views import View
from django.views.generic   import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import NewUserForm


class Registration(CreateView):
    model=User
    form_class=NewUserForm
    template_name = 'accounts/register.html'
    
    success_url= '/categories'
    
    

class Profile(View):
    def get(self, request):
        return redirect('categories.index')
    
    
    
    
    
    
    
    
    
    
    
    