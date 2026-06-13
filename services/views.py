from rest_framework import generics

from .models import Service

from .serializer import ServiceSerialize


class ServiceListView(generics.ListAPIView):

    queryset = Service.objects.filter(is_active=True)

    serializer_class = ServiceSerialize


class ServiceDetailView(
    generics.RetrieveAPIView
):

    queryset = Service.objects.filter(
        is_active=True
    )

    serializer_class = ServiceSerialize