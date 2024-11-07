from django.urls import path
from . import views


urlpatterns = [
    path('groups/manager/users', views.ManagerUsersView.as_view()),
    path('menu-items', views.AllMenuItem.as_view()),
    path('categories', views.CategoryItem.as_view()),
    path('menu-items/<int:pk>', views.SingleItemView.as_view()),
    path('orders/<int:pk>', views.Single_Order_view.as_view()),
    path('orders', views.Orders_view.as_view()),
    path('cart/menu-items', views.Customer_Cart.as_view()),
    path('cart/orders', views.Orders_view.as_view()),
]