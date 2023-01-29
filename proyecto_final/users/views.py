from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from users.forms import RegisterForm, UserUpdateForm


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
            form.save() 
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
        form = UserUpdateForm(initial = {
            'username':user.username
        })
        context ={
            'form':form
        }
        return render(request, 'users/update.html', context=context)

    elif request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':RegisterForm()
        }
        return render(request, 'users/update.html', context=context)