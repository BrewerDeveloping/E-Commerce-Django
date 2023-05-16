from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from . models import Product, Category, Shopping_cart
from django.template.defaultfilters import register

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def category(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=id)
    context = {'products': products, 'category': category,}
    return render(request, 'pages/category.html', context)

def product(request, name):
    product = get_object_or_404(Product, name=name)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'pages/product.html', context)



def search_results(request):
    query = request.GET.get('q')
    if not query:
        products = []
    else:
        products = Product.objects.filter(Q(name__icontains=query))
    context = {
        'query': query,
        'products': products
    }
    return render(request, 'pages/search_results.html', context)




def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    quantity = int(request.POST['quantity'])
    cart_item, created = Shopping_cart.objects.get_or_create(product_id=product)
    cart_item.quantity += quantity
    cart_item.save()
    return redirect('shopping_cart')

def remove_from_cart(request, product_id):
    cart_item = Shopping_cart.objects.get(product_id=product_id)
    cart_item.delete()
    return redirect('shopping_cart')

def shopping_cart(request):
    cart_items = Shopping_cart.objects.all()
    total_cost = sum(item.product_id.cost * item.quantity for item in cart_items)
    context = {'cart_items': cart_items, 'total_cost': total_cost}
    return render(request, 'pages/shopping-cart.html', context)

@register.filter
def multiply(value, arg):
    return value * arg