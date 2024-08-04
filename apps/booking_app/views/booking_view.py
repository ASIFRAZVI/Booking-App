from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.authentication_app.models.user_model import CustomUser
from apps.booking_app.models.booking_model import Train, Booking
from apps.booking_app.serializers.booking_serializer import TrainGetSerializer, BookingSerializer


class TrainAV(APIView):
    def get(self, request, pk=None):
        try:
            if pk is None:
                trains = Train.objects.all()
                serializer = TrainGetSerializer(trains, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            trains=Train.objects.get(pk=pk)
            serializer = TrainGetSerializer(trains)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error":"faild to get train"}, status=400)
        

class BookingAV(APIView):
    def post(self, request):
        data=request.data
        seializer=BookingSerializer(data=data)
        if not seializer.is_valid():
            return Response({"errors":seializer.errors}, status=404)
        
        seializer.save()
        return Response({"ok":"ohoo! Ticket Booked"}, status=201)

    