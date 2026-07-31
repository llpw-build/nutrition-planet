from django.shortcuts import render, get_object_or_404
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

def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        is_active=True,
    )

    context = {
        "product": product,
    }

    return render(
        request,
        "products/product_detail.html",
        context,
    )