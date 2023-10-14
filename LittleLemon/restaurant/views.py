from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking,MenuItem
from .serializers import MenuItemSerializer,BookingSerializer,UserSerializer
from rest_framework import generics
# Create your views here.

class BookingView(APIView):
    def get(self,request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items,many=True)
        return Response(serializer.data)
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)