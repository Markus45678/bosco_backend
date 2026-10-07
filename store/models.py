from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Назва")
    category = models.CharField(max_length=100, verbose_name="Категорія")
    weight_grams = models.PositiveIntegerField(verbose_name="Вага (г)")
    expiry_date = models.DateField(verbose_name="Термін придатності")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна (грн)")

    def __str__(self):
        return f"{self.name} ({self.category})"