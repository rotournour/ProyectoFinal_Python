from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


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
        form = UserCreationForm()
        context ={
            'form':form
        }
        return render(request, 'users/register.html', context=context)

    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
        
        context = {
            'errors':form.errors,
            'form':UserCreationForm()
        }
        return render(request, 'users/register.html', context=context)