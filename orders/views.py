

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import Order, OrderItem

@login_required
def cart_view(request):
    order = Order.objects.filter(user=request.user, completed=False).first()
    
    if order:  
        items = order.items.all()
        total = sum([item.total_price() for item in items])
    else:  
        items = []
        total = 0

    return render(request, 'orders/cart.html', {
        'order': order,
        'items': items,
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
   
    order = Order.objects.filter(user=request.user, completed=False).first()
    if not order:
        order = Order.objects.create(user=request.user, completed=False)
    
    
    order_item, created_item = OrderItem.objects.get_or_create(order=order, product=product)
    if not created_item:
        order_item.quantity += 1
        order_item.save()
    
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    
    order = Order.objects.filter(user=request.user, completed=False).first()
    
    if not order:
        
        return redirect('cart')  
    
    
    order.completed = True
    order.save()
    
    return render(request, 'orders/checkout.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user, completed=True, paid=False)
    return render(request, 'orders/my_orders.html', {'orders': orders})

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.completed = False  
    order.save()
    return redirect('my_orders')

@login_required
def update_order_item(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user)
    if request.method == "POST":
        qty = int(request.POST.get('quantity', 1))
        item.quantity = qty
        item.save()
    return redirect('my_orders')

@login_required
def payment(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user,
        completed=True,
        paid=False
    )

    total = sum(item.total_price() for item in order.items.all())

    if request.method == "POST":
        order.paid = True
        order.save()
        return redirect('payment_success')

    return render(request, 'orders/payment.html', {
        'order': order,
        'total': total
    })

@login_required
def payment_success(request):
    return render(request, 'orders/payment_success.html')