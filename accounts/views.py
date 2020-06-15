from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        # Login User
        print(' ')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        messages.error(request, 'Test')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    return redirect(request, 'accounts/index.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
