from django.urls import path
from shopping_cart.views import cart_summary, cart_add, cart_delete, cart_update, OrderHistory, submit_order

app_name = 'cart'

urlpatterns = [
    path('', cart_summary, name='cart_summary'),
    path('add/', cart_add, name='cart_add'),
    path('delete/', cart_delete, name='cart_delete'),
    path('update/', cart_update, name='cart_update'),
    path('orders/', OrderHistory.as_view(), name='orders'),
    path('submit_order/', submit_order, name='submit_order')
]