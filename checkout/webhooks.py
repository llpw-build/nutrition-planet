import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WH_SECRET,
        )

    except ValueError:
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    event_type = event["type"]

    if event_type == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]

        try:
            order = Order.objects.get(
                stripe_payment_intent_id=payment_intent.id
            )

        except Order.DoesNotExist:
            return HttpResponse(status=200)

        if order.payment_status != "paid":

            for lineitem in order.lineitems.all():
                product = lineitem.product

                product.stock_quantity = (
                    product.stock_quantity - lineitem.quantity
                )

                product.save()

            order.payment_status = "paid"
            order.save()

    elif event_type == "payment_intent.payment_failed":
        payment_intent = event["data"]["object"]

        try:
            order = Order.objects.get(
                stripe_payment_intent_id=payment_intent.id
            )

        except Order.DoesNotExist:
            return HttpResponse(status=200)

        order.payment_status = "failed"
        order.save()

    return HttpResponse(status=200)