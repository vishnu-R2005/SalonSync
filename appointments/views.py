from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Appointment
from .serializers import AppointmentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class BookAppointmentView(
    generics.CreateAPIView
):

    queryset = Appointment.objects.all()

    serializer_class = AppointmentSerializer

    permission_classes = [
        IsAuthenticated
    ]

class MyAppointmentsView(generics.ListAPIView):

    serializer_class = AppointmentSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return Appointment.objects.filter(
            customer=self.request.user
        ).order_by(
            "-appointment_date"
        )
    

class CancelAppointmentView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(self, request, pk):

        appointment = Appointment.objects.get(
            id=pk,
            customer=request.user
        )

        if appointment.status != "pending":

            return Response(
                {
                    "error":
                    "Only pending appointments can be cancelled."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        appointment.status = "cancelled"

        appointment.save()

        return Response(
            {
                "message":
                "Appointment cancelled successfully"
            },
            status=status.HTTP_200_OK
        )