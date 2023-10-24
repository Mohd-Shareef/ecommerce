from django.urls import path
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('main/', views.main, name="main"),
	path('cart/', views.cart, name="cart"),
    path('', views.store, name="store"),
    path('login/', views.Login, name="login"),
	path('checkout/', views.checkout, name="checkout"),
    path('products/<int:myid>', views.productview, name="productview"),
    path('signup/', views.signup, name="signup"),
    path('contactus/', views.contact, name="contactus"),
    path('logout/', views.Logout, name="logout"),
    path('search/', views.search, name="search"),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name="add_to_cart"),
    path('remove_cart/<int:product_id>', views.remove_cart, name="remove_cart"),
    

]