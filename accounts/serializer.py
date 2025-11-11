from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name", "role", "host"]

        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }

    def create(self, validated_data) -> User:
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data.get('role', 'JUNIOR'),
            host=validated_data.get('host','ATIVOS')
        )
        return user

    