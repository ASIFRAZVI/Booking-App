from django.contrib import admin
from apps.booking_app.models.booking_model import Train, Booking, Day

# Register your models here.
admin.site.register(Train)
# admin.site.register(Seat)
admin.site.register(Booking)
admin.site.register(Day)