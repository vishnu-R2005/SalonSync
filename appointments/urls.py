from django.urls import path
from .views import (
    BookAppointmentView,
    MyAppointmentsView,
    CancelAppointmentView
)

from .views import (
    BookAppointmentView,
)

urlpatterns = [

    path(
        "book/",
        BookAppointmentView.as_view(),
        name="book-appointment"
    ),

    path(
        "my/",
        MyAppointmentsView.as_view(),
        name="my-appointments"
    ),

    path(
        "<int:pk>/cancel/",
        CancelAppointmentView.as_view(),
        name="cancel-appointment"
    ),
]