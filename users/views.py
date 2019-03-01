from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

def register(request):
    form  = UserCreationForm()
    return render(request, 'home/register.html', {'forms':form})

def logout_view(request):
    logout(request)
    context = RequestContext(request)
    # Redirect to a success page.
    return render(request, 'home/login.html')