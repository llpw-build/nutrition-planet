from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from products.models import Product

# Create your views here.

def add_to_bag(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
    )

    try:
        quantity = int(
            request.POST.get("quantity")
        )

    except (TypeError, ValueError):
        messages.error(
            request,
            "Please enter a valid quantity.",
        )

        return redirect(
            "product_detail",
            product_id=product.id,
        )

    if quantity < 1:
        messages.error(
            request,
            "Quantity must be at least 1.",
        )

        return redirect(
            "product_detail",
            product_id=product.id,
        )

    bag = request.session.get(
        "bag",
        {},
    )

    product_id = str(product_id)

    if product_id in bag:
        bag[product_id] += quantity

    else:
        bag[product_id] = quantity

    request.session["bag"] = bag

    messages.success(
        request,
        f"{product.name} added to your bag.",
    )

    return redirect(
        "product_detail",
        product_id=product.id,
    )