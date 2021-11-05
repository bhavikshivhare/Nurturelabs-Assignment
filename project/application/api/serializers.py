from rest_framework import fields, serializers
from application.models import Advisor,Booking
from django.contrib.auth.models import User

class BookingSerializer(serializers.ModelSerializer):
    
    booking_id = serializers.StringRelatedField(read_only=True,many=True)

    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ("booked_id",)


class AdvisorSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Advisor
        fields  = "__all__"
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.save()
        return user
    