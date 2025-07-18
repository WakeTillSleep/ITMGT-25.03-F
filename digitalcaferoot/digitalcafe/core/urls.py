from django.urls import path
from . import views

urlpatterns = [
    path("accounts/login/", views.login_view, name="login_view"),
    path("", views.index, name="index"),
    path("product/<int:product_id>", views.product_detail, name="product_detail"),
    path("checkout", views.checkout, name="checkout"),
    path("transactions", views.transaction_history, name="transaction_history"),
]