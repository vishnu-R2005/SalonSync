from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True
                                     )
    
    class Meta:

        model = User

        fields=(
            "id",
            "username",
            "email",
            "phone",
            "role",
            "password"

        )


    def create(self,validated_data):
        user = User(**validated_data)
        password = validated_data.pop("password")

        user.set_password("password")

        user.save()

        return user
    
    
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "email",
            "phone",
            "role"
        )