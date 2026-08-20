from django import forms
from .models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

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

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = (
            "rating",
            "comment",
        )