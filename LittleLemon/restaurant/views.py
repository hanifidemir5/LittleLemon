from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Booking,MenuItem
from .serializers import MenuItemSerializer,BookingSerializer,UserSerializer
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"anime girls is not real"})

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get(self,request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items,many=True)
        return Response(serializer.data)
    
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)