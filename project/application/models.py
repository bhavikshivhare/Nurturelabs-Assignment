from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Advisor
class Advisor(models.Model):
    advisor_name = models.CharField(max_length=30,blank=False)
    advisor_photo = models.ImageField(null=True,blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.advisor_name


class Booking(models.Model):
    booked_id = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=False)


# def __str__(self):
#     return self.booked_id
