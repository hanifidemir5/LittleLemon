from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('booking/',views.BookingViewSet.as_view({'get':'list'})),
    path('users/',views.UserViewSet.as_view({'get':'list'})),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>',views.SingleMenuItemView.as_view()),
    path('animegirls',views.msg),
    path('api-token-auth/',obtain_auth_token),
]