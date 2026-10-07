import random
from datetime import date, timedelta
from django.http import HttpResponse
from .models import Product


def products_list(request):

    products = Product.objects.all()

    rows = ""
    for p in products:
        rows += f"""
        <tr>
            <td>{p.id}</td>
            <td><strong>{p.name}</strong></td>
            <td>{p.category}</td>
            <td>{p.weight_grams} г</td>
            <td>{p.expiry_date}</td>
            <td>{p.price} грн</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Склад продуктів</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 30px; background-color: #f8f9fa; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; max-width: 900px; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.2); }}
            th, td {{ border: 1px solid #ddd; padding: 10px 14px; text-align: left; }}
            th {{ background-color: #007bff; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Список товарів на складі</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Назва</th>
                    <th>Категорія</th>
                    <th>Вага</th>
                    <th>Термін придатності</th>
                    <th>Ціна</th>
                </tr>
            </thead>
            <tbody>
                {rows if rows else '<tr><td colspan="6">Товари відсутні</td></tr>'}
            </tbody>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)


def replenish_stock(request, count):

    sample_names = [
        ("Сир Гауда", "Молочні продукти"),
        ("Молоко Ультрапастеризоване", "Молочні продукти"),
        ("Шоколад Крафтовий", "Солодощі"),
        ("Кефір 1%", "Молочні продукти"),
        ("Багет Французький", "Випічка"),
        ("Зефір", "Солодощі"),
        ("Сок Апельсиновий", "Напої")
    ]

    new_items = []
    for _ in range(count):
        name, category = random.choice(sample_names)
        weight = random.randint(100, 1000)
        days_valid = random.randint(5, 365)
        expiry = date.today() + timedelta(days=days_valid)
        price = round(random.uniform(20.0, 250.0), 2)

        new_items.append(Product(
            name=f"{name} (Лот {random.randint(100, 999)})",
            category=category,
            weight_grams=weight,
            expiry_date=expiry,
            price=price
        ))


    Product.objects.bulk_create(new_items)

    return HttpResponse(
        f"<h2>Успішно додано {count} нових записів до бази даних!</h2>"
        f'<p><a href="/products">Перейти до списку товарів</a></p>'
    )