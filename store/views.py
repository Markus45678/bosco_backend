from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/products.html', {'products': products})

def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        if name and quantity and price:
            Product.objects.create(
                name=name,
                quantity=quantity,
                price=price
            )
            messages.success(request, f'Товар "{name}" успішно додано!')
            return redirect('product_list')  # Post/Redirect/Get
        else:
            messages.error(request, 'Будь ласка, заповніть усі поля форми.')

    return render(request, 'inventory/product_add.html')