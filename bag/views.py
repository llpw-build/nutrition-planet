from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
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

    current_quantity = bag.get(
        product_id,
        0,
    )
    new_quantity = current_quantity + quantity

    if new_quantity > product.stock_quantity:
        messages.error(
            request,
            f"Only {product.stock_quantity} of "
            f"{product.name} are available.",
        )

        return redirect(
            "product_detail",
            product_id=product.id,
        )

    bag[product_id] = new_quantity

    request.session["bag"] = bag

    messages.success(
        request,
        f"{product.name} added to your bag.",
    )

    return redirect(
        "product_detail",
        product_id=product.id,
    )


def view_bag(request):
    return render(
        request,
        "bag/bag.html",
    )


def update_bag(request, product_id):

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
            "view_bag"
        )

    if quantity < 1:
        messages.error(
            request,
            "Quantity must be at least 1.",
        )

        return redirect(
            "view_bag"
        )

    if quantity > product.stock_quantity:
        messages.error(
            request,
            f"Only {product.stock_quantity} of "
            f"{product.name} are available.",
        )

        return redirect(
            "view_bag"
        )

    bag = request.session.get(
        "bag",
        {},
    )

    product_id = str(product_id)

    bag[product_id] = quantity

    request.session["bag"] = bag

    messages.success(
        request,
        "Bag successfully updated.",
    )

    return redirect(
        "view_bag"
    )


def remove_from_bag(request, product_id):

    bag = request.session.get(
        "bag",
        {},
    )

    product_id = str(product_id)

    if product_id in bag:
        del bag[product_id]

    request.session["bag"] = bag

    messages.success(
        request,
        "Product removed successfully",
    )

    return redirect(
        "view_bag"
    )