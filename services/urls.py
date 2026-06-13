from django.urls import path 

from .views import (ServiceListView,ServiceDetailView)
from .views import ServiceUpdateDeleteView,ServiceCreateView

urlpatterns = [
    path("",ServiceListView.as_view(),name="service-list"),
    path("<int:pk>/",ServiceDetailView.as_view(),name="service-detail"),
    path("create/",ServiceCreateView.as_view(),name="service-create"),
    path("<int:pk>/manage/",ServiceUpdateDeleteView.as_view(),name="service-manage"),
]
