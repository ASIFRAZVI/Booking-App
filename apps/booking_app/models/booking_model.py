from django.db import models
from django.utils import timezone
from apps.authentication_app.models.user_model import BaseModel, CustomUser
from django.core.exceptions import ValidationError


from django.db import models

class Day(BaseModel):
    name = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return self.name


class Train(BaseModel):
    train_number = models.CharField(max_length=20, unique=True)
    train_name=models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField(default=timezone.now)
    arrival_time = models.TimeField(default=timezone.now)   
    total_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default=0)
    running_days = models.ManyToManyField(Day, related_name='days')

    def __str__(self):
        return self.train_name
    
    
class Booking(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customuser")
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name="trains")
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    seat_number=models.IntegerField()
    booking_date = models.DateField()

