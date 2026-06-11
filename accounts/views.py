from django.shortcuts import render

# Create your views here.


from rest_framework import gerneric
from .serializer import RegisterSerializer
from .serializer import ProfileSerializer
from .models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

class RegisterView(gerneric.CreateAPIView):

    queryset=User.objects.all()

    serializer_class = RegisterSerializer


class profileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self , reuest):
        Serializer = ProfileSerializer(
            request.user
        )

        return Response(Serializer.data)
    
