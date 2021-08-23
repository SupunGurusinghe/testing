from django.urls import path
from . import views

urlpatterns = [
	path('cart/', views.carts,name="cart"),
	path('store/',views.store,name="store"),
	path('checkout/',views.checkout,name="checkout")

]