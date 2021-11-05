
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from rest_framework import (generics, mixins, permissions, serializers, status,
                            viewsets)
from rest_framework.decorators import action
from rest_framework.generics import  get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from application.api.serializers import (AdvisorSerializer, BookingSerializer,
                                         UserSerializer)
from application.models import Advisor, Booking


# Create your views here.
class CreateAdvisorAPIView(generics.CreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
    

    def post(self, request):
        serializer = AdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



class RegisterAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListAdvisorAPIView(generics.ListCreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingCallAPIView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_pk'

    @action(detail=True, methods=['post'])
    def create(self,serializer):
        advisor_pk = self.kwargs.get("advisor_pk")
        book = get_object_or_404(Advisor, pk=advisor_pk)
        booking_id = self.request.user
        serializer.save(book=book, booking_id=booking_id)
        return  Response(serializer.data, status=status.HTTP_200_OK)

        
  
