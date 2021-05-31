from rest_framework import serializers

from profiles_api import models

class TextSerializer(serializers.Serializer):
    """
    Serializes a name field for our TextView
    """
    name = serializers.CharField(max_length = 10)

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serialize a User Profile
    """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input':'password'
                }
            }
        }

        def create(self, validated_data):
            """
            Create and return a new user, in this used for the password hash
            """
            user = models.UserProfile.objects.create_user(
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password']
            )
            return user

        def update(self, instance, validated_data):
            """
            Handle updating user account
            """
            if 'password' in validated_data:
                password = validated_data.pop('password')
                instance.set_password(password)
    
            return super().update(instance, validated_data)
