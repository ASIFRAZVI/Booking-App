from rest_framework import serializers
from apps.authentication_app.models.user_model import CustomUser
from apps.booking_app.models.booking_model import Train, Day, Booking


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Day
        fields=["id", "name"]


class TrainGetSerializer(serializers.ModelSerializer):
    running_days=DaySerializer(many=True)
    class Meta:
        model =Train
        fields="__all__"


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.UUIDField()
    train = serializers.UUIDField()

    class Meta:
        model=Booking
        fields="__all__"

    def validate_user(self, value):
        if not value:
            raise serializers.ValidationError("Must be a valid user.")
        user=CustomUser.objects.get(id=value)
        user_status=user.is_active
        if not user_status:
            raise serializers.ValidationError("User is not active.")
        return user

    def validate_train(self, value):
        if not value:
            raise serializers.ValidationError("Must be a valid train.")
        return Train.objects.get(id=value)
    
    def validate(self, value):
        source_input=value["source"]
        destination_input=value["destination"]
        print(source_input)

        # train_data=Train.objects.get(id=value)
        # original_source=train_data.source
        # original_destination=train_data.destination

        # if not (source_input.lower() == original_source.lower() and 
        #         destination_input.lower() == original_destination.lower()):
        #     raise serializers.ValidationError("The train does not start and end at the specified locations.")

        # return value

    def validate(self, value):
        seat_input=value.get('seat_number')  
        train_name_input = value.get('train')
        try:
            train = Train.objects.get(train_name=train_name_input)
            total_seats = train.total_seats
            if seat_input > total_seats:
                raise serializers.ValidationError("Invalid Seat number")
            
        except Train.DoesNotExist:
            raise serializers.ValidationError("Invalid train ID.")
        return value
            