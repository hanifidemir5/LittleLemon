from django.urls import path,include
from .views import BookingView,MenuItemsView,UserViewSet,SingleMenuItemView

urlpatterns = [
    path('booking/',BookingView.as_view()),
    path('users/',UserViewSet.as_view()),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]