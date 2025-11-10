from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('menu/<int:pk>/', views.menu_detail, name="menu_detail"),
    path("cart/", views.cart_view, name="cart_view"),
    path("cart/add/<int:pk>/", views.cart_add, name="cart_add"),
    path("cart/remove/<int:pk>/", views.cart_remove, name="cart_remove"),
    path("cart/clear/", views.cart_clear, name="cart_clear"),
    path("cart/update/<int:pk>/", views.cart_update, name="cart_update"),
    path("cart/order/", views.order_view, name="order_view"),
]
