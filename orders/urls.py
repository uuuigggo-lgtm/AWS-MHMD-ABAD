from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart, checkout , my_orders,cancel_order,update_order_item,payment,payment_success

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('my-orders/', my_orders, name='my_orders'),
    path('cancel-order/<int:order_id>/', cancel_order, name='cancel_order'),
    path('update-order-item/<int:item_id>/', update_order_item, name='update_order_item'),
    path('payment/<int:order_id>/', payment, name='payment'),
    path('payment-success/', payment_success, name='payment_success'),

]