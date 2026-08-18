from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem
import stripe
from django.conf import settings
from django.http import JsonResponse


def checkout(request):

    bag = request.session.get(
        "bag",
        {},
    )

    total = 0

    for product_id, quantity in bag.items():
        product = get_object_or_404(
            Product,
            id=product_id,
        )

        total += product.price * quantity

    stripe_total = int(total * 100)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    intent = stripe.PaymentIntent.create(
    amount=stripe_total,
    currency="gbp",
    )

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()

            payment_intent_id = request.POST.get(
                "payment_intent_id"
             )

            order.stripe_payment_intent_id = payment_intent_id
            order.save()

            stripe.PaymentIntent.modify(
            payment_intent_id,
            metadata={
                "order_id": str(order.id),
            },
            )


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

                return JsonResponse(
                    {
                        "order_id": order.id,
                    }
                )

            

    else:
        form = OrderForm()

    context = {
        "form": form,
        "client_secret" : intent.client_secret,
        "stripe_public_key" : settings.STRIPE_PUBLIC_KEY,
        "payment_intent_id": intent.id,
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

    request.session.pop("bag", None)

    messages.success(
        request,
        "Your order was placed successfully!",
    )

    context = {
        "order": order,
    }

    return render(
        request,
        "checkout/checkout_success.html",
        context,
    )

def checkout_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
    )

    request.session.pop("bag", None)

    messages.success(
        request,
        "Your order was placed successfully!",
    )

    context = {
        "order": order,
    }

    return render(
        request,
        "checkout/checkout_success.html",
        context,
    )