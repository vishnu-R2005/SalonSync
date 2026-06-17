from django.db import models


class Employee(models.Model):
    ROLE_CHOICES = [
        ('stylist', 'Stylist'),
        ('receptionist', 'Receptionist'),
        ('manager', 'Manager'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    experience_years = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"