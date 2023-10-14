from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer

# Create your views here.

class BookingView(APIView):
    def get(self,request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items,many=True)
        return Response(serializer.data)
    
class MenuView(APIView):
    def get(self,request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items,many=True)
        return Response(serializer.data)