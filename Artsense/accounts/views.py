# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saves user with hashed password
            # Auto-login after signup
            login(request, user)
            return redirect('/showarts')  # Go to profile after signup
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign_up.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('showarts')
        else:
            error = "Invalid username or password"
    return render(request, 'accounts/login.html', {'error': error})

def profile_view(request):
    return render(request, 'accounts/profile.html')