from rest_framework import serializers
from datetime import datetime, timedelta

from .models import Appointment
from services.models import Service
class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = "__all__"

        read_only_fields = (
            "customer",
            "end_time",
            "status",
        )
    
    def validate(self, attrs):

            service = attrs["service"]

            appointment_date = attrs["appointment_date"]

            start_time = attrs["start_time"]

            start_datetime = datetime.combine(
                appointment_date,
                start_time
            )

            end_datetime = start_datetime + timedelta(
                minutes=service.duration_minuts
            )

            end_time = end_datetime.time()

            existing_appointments = Appointment.objects.filter(
                appointment_date=appointment_date
            ).exclude(
                status="cancelled"
            )

            for appointment in existing_appointments:

                if (
                    start_time < appointment.end_time
                    and
                    end_time > appointment.start_time
                ):

                    raise serializers.ValidationError(
                        "This time slot is already booked."
                    )

            return attrs


    def create(self, validated_data):

        request = self.context["request"]

        customer = request.user

        service = validated_data["service"]

        appointment_date = validated_data["appointment_date"]

        start_time = validated_data["start_time"]

        start_datetime = datetime.combine(
            appointment_date,
            start_time
        )

        end_datetime = start_datetime + timedelta(
            minutes=service.duration_minuts
        )

        end_time = end_datetime.time()

        appointment = Appointment.objects.create(
            customer=customer,
            service=service,
            appointment_date=appointment_date,
            start_time=start_time,
            end_time=end_time,
            notes=validated_data.get("notes", "")
        )

        return appointment