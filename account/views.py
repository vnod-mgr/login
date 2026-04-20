from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User
from .forms import UserForm, LoginForm, CheckForm
from default.models import check_form

def get_ip(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if User.objects.filter(email=data['email']).exists():
                form.add_error('email', 'This email already exists.')
                return render(request, 'main/register.html', {'form': form})
            User.objects.create(
                username = data['username'],
                email    = data['email'],
                password = make_password(data['password1']),
            )
            messages.success(request, 'Account created! Please login.')
            return redirect('login')
        return render(request, 'main/register.html', {'form': form})
    form = UserForm()
    return render(request, 'main/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data     = form.cleaned_data
            email    = data['email']
            password = data['password']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error('email', 'Email not found.')
                return render(request, 'main/login.html', {'form': form})
            if check_password(password, user.password):
                request.session['user_id']  = user.id
                request.session['username'] = user.username
                request.session['email']    = user.email
                messages.success(request, f'Welcome back {user.username}!')
                return redirect('home')
            else:
                form.add_error('password', 'Incorrect password.')
                return render(request, 'main/login.html', {'form': form})
    form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_clear(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully.')
    return redirect('login')

def checkformview(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            check_form.objects.create(
                name       = data['name'],
                email      = data['email'],
                message    = data['message'],
                ip_address = get_ip(request),
            )
            messages.success(request, 'Message sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please fix the errors below.')
        return render(request, 'main/checkform.html', {'form': form})
    form = CheckForm()
    return render(request, 'main/checkform.html', {'form': form})
