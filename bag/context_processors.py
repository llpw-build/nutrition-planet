from products.models import Product
from django.shortcuts import get_object_or_404


def bag_contents(request):
    bag = request.session.get("bag", {})

    bag_items = []
    bag_count = sum(bag.values())
    total = 0

    for product_id, quantity in bag.items():
        product = get_object_or_404(
            Product,
            id=product_id,
        )

        line_total = product.price * quantity
        total += line_total

        bag_items.append(
            {
                "product": product,
                "quantity": quantity,
                "line_total": line_total,
            }
        )

    return {
        "bag_items": bag_items,
        "bag_count": bag_count,
        "total": total,
    }