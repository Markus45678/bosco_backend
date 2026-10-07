from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})

def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        weight_grams = request.POST.get('weight_grams')
        expiry_date = request.POST.get('expiry_date')
        price = request.POST.get('price')

        if name and category and weight_grams and expiry_date and price:
            Product.objects.create(
                name=name,
                category=category,
                weight_grams=weight_grams,
                expiry_date=expiry_date,
                price=price
            )
            messages.success(request, f'Товар "{name}" успішно додано!')
            return redirect('product_list')
        else:
            messages.error(request, 'Будь ласка, заповніть усі поля форми.')

    return render(request, 'store/product_add.html')