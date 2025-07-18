from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from .models import Product
from .models import Product, CartItem
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
import datetime as dt
from .models import Transaction, LineItem
from .models import CartItem, Transaction, LineItem


@login_required
def index(request):
    # Get cart items for the logged-in user
    cart_items = CartItem.objects.filter(user=request.user)

    # Get all available products
    products = Product.objects.all()

    return render(request, "core/index.html", {
        "cart_items": cart_items,
        "products": products,
    })


@login_required
def product_detail(request, product_id):
    if request.method == 'GET':
        template = loader.get_template("core/product_detail.html")
        p = get_object_or_404(Product, id=product_id)
        context = {
            "product": p
        }
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        submitted_quantity = request.POST['quantity']
        submitted_product_id = request.POST['product_id']
        product = get_object_or_404(Product, id=submitted_product_id)
        user = request.user
        cart_item = CartItem(user=user, product=product, quantity=submitted_quantity)
        cart_item.save()

        messages.add_message(
            request,
            messages.INFO,
            f'Added {submitted_quantity} of {product.name} to your cart'
        )
        return redirect('index')

def login_view(request):
    if request.method == 'GET':
        template = loader.get_template("core/login_view.html")
        context = {}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        submitted_username = request.POST['username']
        submitted_password = request.POST['password']
        user_object = authenticate(
            username=submitted_username,
            password=submitted_password
        )
        if user_object is None:
            messages.add_message(request, messages.INFO, 'Invalid login.')
            return redirect(request.path_info)
        login(request, user_object)
        return redirect('index')

@login_required
def checkout(request):
    if request.method == 'GET':
        template = loader.get_template("core/checkout.html")
        cart_items = CartItem.objects.filter(user=request.user)
        context = {
            'cart_items': list(cart_items),
        }
        return HttpResponse(template.render(context, request))
    
    elif request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        
        # Create transaction
        created_at = dt.datetime.now(tz=dt.timezone.utc)
        transaction = Transaction(user=request.user, created_at=created_at)
        transaction.save()
        
        # Convert CartItems to LineItems
        for cart_item in cart_items:
            line_item = LineItem(
                transaction=transaction,
                product=cart_item.product,
                quantity=cart_item.quantity,
            )
            line_item.save()
            cart_item.delete()
        
        messages.add_message(request, messages.INFO, 'Thank you for your purchase!')
        return redirect('index')

@login_required
def transaction_history(request):
    # Get user's transactions
    transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')

    # For each transaction, get its line items
    transaction_data = []
    for transaction in transactions:
        line_items = LineItem.objects.filter(transaction=transaction)
        transaction_data.append({
            'transaction': transaction,
            'line_items': line_items
        })

    return render(request, 'core/transaction_history.html', {
        'transaction_data': transaction_data
    })