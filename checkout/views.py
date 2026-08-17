from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem

def checkout(request):

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()

            bag = request.session.get(
                "bag",
                {},
            )

            for product_id, quantity in bag.items():

                product = get_object_or_404(
                    Product,
                    id=product_id,
                )

                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                )

            del request.session["bag"]

            messages.success(
                request,
                "Your order was placed successfully!",
            )

            return redirect(
                "checkout_success",
                order_id=order.id,
            )

    else:
        form = OrderForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "checkout/checkout.html",
        context,
    )


def checkout_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
    )

    context = {
        "order": order,
    }

    return render(
        request,
        "checkout/checkout_success.html",
        context,
    )