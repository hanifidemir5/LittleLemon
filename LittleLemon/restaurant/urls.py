from django.urls import path,include
from .views import BookingView,MenuView

urlpatterns = [
    path('menu/',MenuView.as_view()),
    path('booking/',BookingView.as_view()),
]