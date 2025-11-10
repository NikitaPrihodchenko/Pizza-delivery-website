from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from django.views.decorators.http import require_POST
from .forms import OrderForm


def index(request):
    categories = Category.objects.prefetch_related("products").all()
    return render(request, "menu/index.html", {"categories": categories})


def about(request):
    return render(request, "menu/about.html")


def contact(request):
    return render(request, "menu/contact.html")


def menu_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "menu/menu_detail.html", {"product": product})


@require_POST
def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart = request.session.get("cart", {})

    if str(pk) in cart:
        cart[str(pk)]["quantity"] += 1
    else:
        cart[str(pk)] = {
            "name": product.name,
            "price": float(product.price),
            "quantity": 1,
            "image": product.image.url if product.image else None,
        }

    request.session["cart"] = cart
    request.session.modified = True

    total_items = sum(item["quantity"] for item in cart.values())

    if request.headers.get("HX-Request"):
        return render(request, "menu/cart_count.html", {"total_items": total_items})

    return redirect(request.META.get("HTTP_REFERER", "/"))


def cart_view(request):
    cart = request.session.get("cart", {})
    total = sum(item["price"] * item["quantity"] for item in cart.values())
    return render(request, "menu/cart.html", {"cart": cart, "total": total})


def cart_remove(request, pk):
    cart = request.session.get("cart", {})

    if str(pk) in cart:
        del cart[str(pk)]

    request.session["cart"] = cart
    return redirect("cart_view")


@require_POST
def cart_clear(request):
    request.session["cart"] = {}
    request.session.modified = True

    if request.headers.get("HX-Request"):
        return render(request, "menu/cart_content.html", {"total": 0, "cart": {}})

    return redirect(request.META.get("HTTP_REFERER", "/"))


def cart_update(request, pk):
    cart = request.session.get("cart", {})
    quantity = int(request.POST.get("quantity", 1))

    if str(pk) in cart:
        cart[str(pk)]["quantity"] = max(1, quantity)

    request.session["cart"] = cart
    return redirect("cart_view")


def menu_index(request):
    categories = Category.objects.prefetch_related("products").all()
    cart = request.session.get("cart", {})
    cart_total = sum(item["quantity"] for item in cart.values()) if cart else 0
    request.session['cart_total'] = cart_total
    return render(request, "menu/index.html", {"categories": categories, "cart_total": cart_total})


def order_view(request):
    cart = request.session.get("cart", {})

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            request.session["cart"] = {}
            request.session.modified = True
            return render(request, "menu/order_success.html")
    else:
        form = OrderForm()

    return render(request, "menu/order.html", {"form": form, "cart": cart})
