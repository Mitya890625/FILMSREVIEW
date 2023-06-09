from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt

# signup


@csrf_exempt
def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupaccount.html',
                      {'form': UserCreateForm})
    if request.POST.get('password1') == request.POST.get('password2'):
        try:
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password1')
            )
            user.save()
            login(request, user)
            return redirect('/home')
        except IntegrityError:
            return render(
                request,
                'accounts/signupaccount.html',
                {
                    'form': UserCreateForm,
                    'error': 'Username already taken. Choose new username.'
                }
            )
    else:
        return render(
            request, 'accounts/signupaccount.html',
            {
                'form': UserCreateForm,
                'error': 'Passwords do not match'
            }
        )


def logoutaccount(request):
    logout(request)
    return redirect('/home')


@csrf_exempt
def loginaccount(request):
    if request.method == 'GET':
        return render(
            request, 'accounts/loginaccount.html',
            {'form': AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is None:
            return render(
                request, 'accounts/loginaccount.html',
                {
                    'form': AuthenticationForm(),
                    'error': 'username and password do not match'
                }
            )
        else:
            login(request, user)
            return redirect('/home')
