from django import forms

from .models import Product

class ProductForm(forms.ModelsForm):
    class meta:
        Model = Product,

    fields = (
            "name",
            "brand",
            "category",
            "price",
            "size_or_quantity",
            "materials",
            "ingredients",
            "stock_quantity",
            "description",
            "image",
            "is_active",
        )