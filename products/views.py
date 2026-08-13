from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import user_passes_test


from .models import Product, Category
from .forms import ProductForm


def all_products(request):

    products = Product.objects.filter(
        is_active=True,
    )

    query = None
    category = request.GET.get("category")
    sort = request.GET.get("sort")
    direction = request.GET.get("direction")

    if "q" in request.GET:
        query = request.GET.get("q")

        if not query:
            messages.error(
                request,
                "Please enter search criteria.",
            )
        else:
            products = products.filter(
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(brand__name__icontains=query)
                | Q(category__friendly_name__icontains=query)
            )

    if category:
        products = products.filter(
            category__name=category,
        )

    allowed_sort_fields = {
        "name",
        "price",
    }

    if sort in allowed_sort_fields:
        sort_field = sort

        if direction == "desc":
            sort_field = "-" + sort_field

        products = products.order_by(sort_field)

    categories = Category.objects.all()

    context = {
        "products": products,
        "search_term": query,
        "current_category": category,
        "current_sort": sort,
        "current_direction": direction,
        "categories": categories,
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


@user_passes_test(lambda user: user.is_staff)
def add_product(request):

    if request.method == "POST":
        form = ProductForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            product = form.save()

            messages.success(
                request,
                "Successfully added product.",
            )

            return redirect(
                "product_detail",
                product_id=product.id,
            )

    else:
        form = ProductForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "products/add_product.html",
        context,
    )

@user_passes_test(lambda user: user.is_staff)
def edit_product(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
    )

    if request.method == "POST":
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Product updated successfully.",
            )

            return redirect(
                "product_detail",
                product_id=product.id,
            )

    else:
        form = ProductForm(
            instance=product,
        )

    context = {
        "form": form,
        "product": product,
    }

    return render(
        request,
        "products/edit_product.html",
        context,
    )

@user_passes_test(lambda user: user.is_staff)
def delete_product(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
    )

    if request.method == "POST":
        product.delete()

        messages.success(
            request,
            "Product deleted successfully.",
        )

        return redirect("all_products")

    context = {
        "product": product,
    }

    return render(
        request,
        "products/delete_product.html",
        context,
    )