from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from users.forms import RegisterForm, UpdateForm, ProfileForm
from users.models import UserProfile


def user_login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'users/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                context = {
                    'message':f'Bienvenido/a a VintageStore {username}.'
                }
                return render(request, 'index.html', context=context)

        form = AuthenticationForm()
        context ={
            'form':form,
            'errors':'Tu usuario y/o contraseña son incorrectos. Vuelve a introducirlos'
        }
        return render(request, 'users/login.html', context=context)
    
    
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context ={
            'form':form
        }
        return render(request, 'users/register.html', context=context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            UserProfile.objects.create(user=user)
            return redirect('login')
        
        context = {
            'errors':form.errors,
            'form':RegisterForm()
        }
        return render(request, 'users/register.html', context=context)
    
    
@login_required
def update_user(request):
    user = request.user
    if request.method == 'GET':
        form = UpdateForm(initial = {
            'username':user.username
        })
        context ={
            'form':form
        }
        return render(request, 'users/update_user.html', context=context)

    elif request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':UpdateForm()
        }
        return render(request, 'users/update_user.html', context=context)
    
    
def update_profile(request):
    user = request.user
    if request.method == 'GET':
        form = ProfileForm(initial={
            'phone':request.user.profile.phone,
            'birth_date':request.user.profile.birth_date,
            'profile_picture':request.user.profile.profile_picture
        })
        context ={
            'form':form
        }
        return render(request, 'users/update_profile.html', context=context)

    elif request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':ProfileForm()
        }
        return render(request, 'users/register.html', context=context)