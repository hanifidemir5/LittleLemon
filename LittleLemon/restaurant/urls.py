from django.urls import path,include
from .views import BookingViewSet,MenuItemsView,UserViewSet,SingleMenuItemView

urlpatterns = [
    path('booking/',BookingViewSet.as_view({'get':'list'})),
    path('users/',UserViewSet.as_view({'get':'list'})),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]