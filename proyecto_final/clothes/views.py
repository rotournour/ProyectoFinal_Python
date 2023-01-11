from django.shortcuts import render
from django.http import HttpResponse
from clothes.models import Clothes, Type_Clothing
from clothes.forms import ClothingForm

def create_clothing (request):
    if request.method == 'GET':
        context = {
            'form': ClothingForm()}
        return render(request,'clothes/create.html', context=context)

    elif request.method == 'POST':
        form = ClothingForm(request.POST)
        if form.is_valid():
            Clothes.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                category = form.cleaned_data['category'],
                brand = form.cleaned_data['brand'],
                gender = form.cleaned_data['gender'],
                new_clothing = form.cleaned_data['new_clothing'],
                stock=form.cleaned_data['stock'],
                
            )
            context = {
                'message': 'Genial! Tu prenda esta lista para su venta'
            }
            return render(request, 'clothes/create.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ClothingForm()
            }
            return render(request, 'clothes/create.html', context=context)
        

def list_categories(request):
    all_categories = Type_Clothing.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'clothes/list_categories.html', context=context)

def list_clothes(request):
    if 'search' in request.GET:
        search = request.GET['search']
        clothes = Clothes.objects.filter(name__icontains=search)
    else:
        clothes = Clothes.objects.all()
    context = {
        'clothes':clothes,
    }
    return render(request, 'clothes/list_clothes.html', context=context)


