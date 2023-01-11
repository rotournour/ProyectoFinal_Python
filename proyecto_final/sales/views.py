from django.shortcuts import render
from sales.forms import SalesForm
from sales.models import Sales

def create_order (request):
    if request.method == 'GET':
        context = {
            'form': SalesForm()}
        return render(request,'sales/order.html', context=context)

    elif request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            Sales.objects.create(
                client=form.cleaned_data['client'],
                clothes_name=form.cleaned_data['clothes_name'],
                category=form.cleaned_data['category'],
                payment=form.cleaned_data['payment']
            )
            context = {
                'message': 'El producto se ha añadido a tu carrito de compras'
            }
            return render(request, 'sales/order.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': SalesForm()
            }
            return render(request, 'sales/order.html', context=context)
        
