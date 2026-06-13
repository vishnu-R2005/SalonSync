from rest_framework import generics

from .models import Service

from .serializer import ServiceSerialize
from .permissions import IsAudminUserRole


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


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()

    serializer_class=ServiceSerialize

    # permission_classes=[
    #     IsAudminUserRole
    # ]

class ServiceUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()

    serializer_class = ServiceSerialize

    # permission_classes=[
    #     IsAudminUserRole
    # ]

