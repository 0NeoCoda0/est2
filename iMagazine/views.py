from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import FoodType, ProductCard, UserCart


def index(request):
    return render(request, 'iMagazine/index.html')


def menu_page(request):
    products = ProductCard.objects.all()
    types = FoodType.objects.all()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'products': products,
        'types': types,
        'num_visits': num_visits,
    }

    return render(request, 'iMagazine/menu-page.html', context)

def user_cart(request):
    cart = get_object_or_404(UserCart, user=request.user)
    cart_items = cart.cartitem_set.all()
    context = {
        'cart': cart,
        'cart_items': cart_items,

    }
    return render(request, 'iMagazine/usercart.html' ,context)

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(ProductCard, id=product_id)
    cart, created = UserCart.objects.get_or_create(user=request.user)
    cart.add_to_cart(product)
    return JsonResponse({'success': True})
