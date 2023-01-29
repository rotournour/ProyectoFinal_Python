from django.shortcuts import render, redirect
from clothes.models import Clothes, Type_Clothing
from clothes.forms import ClothingForm, ClothesCart
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test, login_required

@login_required
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

def list_and_buy(request):
    if request.method == 'GET':
        if 'search' in request.GET:
            search = request.GET['search']
            clothes = Clothes.objects.filter(name__icontains=search)
        else:
            clothes = Clothes.objects.all()
        context = {
            'clothes':clothes,
            'form': ClothesCart(),
        }
        return render(request, 'clothes/list_clothes.html', context=context)
    else:
        form = ClothesCart(request.POST)
        if form.is_valid():
            cloth = Clothes.objects.get(id=form.cleaned_data['cloth'])
            cloth.payment = form.cleaned_data['type_payment']
            cloth.setUnavailable()
            cloth.save()
            context = {
                'message': 'Gracias por añadir el producto a tu carrito de compras! En breve nos pondremos en contacto contigo para procesar el pago :)'
            }
            return render(request, 'sales/pay_order.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ClothesCart()
            }
            return render(request, 'sales/pay_order.html', context=context)

@user_passes_test((lambda u: u.is_superuser))
def clothes_update(request, pk):
    clothes = Clothes.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'form': ClothingForm(
                initial={
                    'name': clothes.name,
                    'price': clothes.price,
                    'category': clothes.category,
                    'brand': clothes.brand,
                    'gender': clothes.gender,
                    'new_clothing': clothes.new_clothing,
                }
            )
        }

        return render(request, 'clothes/update_clothes.html', context=context)

    elif request.method == 'POST':
        form = ClothingForm(request.POST)
        if form.is_valid():
            clothes.price = form.cleaned_data['price']
            clothes.category = form.cleaned_data['category']
            clothes.save()
            
            context = {
                'message': 'Genial! La prenda ha sido actualizada correctamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ClothingForm()
            }
        return render(request, 'clothes/update_clothes.html', context=context)


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser


class ClothesDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Clothes
    template_name = 'clothes/delete_clothes.html'
    success_url = '/clothes/listado_clothes/'

