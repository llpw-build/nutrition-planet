from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):

    products = Product.objects.filter(
        is_active=True
    )

    context = {
        "products": products,
    }

    return render(
        request,
        "products/products.html",
        context,
    )