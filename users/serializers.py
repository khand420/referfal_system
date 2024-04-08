
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Include password as a write-only field

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'referral_code', 'timestamp', 'password']
        extra_kwargs = {
            'timestamp': {'read_only': True},  # Timestamp should be read-only
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Remove password from validated data
        user = User(**validated_data)

        if password is not None:
            user.set_password(password)  # Set and hash the password

        user.save()
        return user





class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        print('attrs------', attrs )
        email = attrs.get('email')
        password = attrs.get('password')
        
        # print(email)

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            print('user-------', user)

            if not user:
                raise serializers.ValidationError("Unable to log in with provided credentials.")

            if not user.is_active:
                raise serializers.ValidationError("User account is disabled.")

            refresh = self.get_token(user)
            data = {
                'email': user.email,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return data

        raise serializers.ValidationError("Must include 'email' and 'password'.")
    





# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'name', 'email', 'referral_code', 'timestamp']




#         fields = ['id', 'username', 'email', 'referral_code', 'registration_timestamp']




    
# class CustomTokenObtainSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         if email and password:
#             user = authenticate(request=self.context.get('request'), email=email, password=password)

#             if not user:
#                 raise serializers.ValidationError("Unable to log in with provided credentials.")

#             if not user.is_active:
#                 raise serializers.ValidationError("User account is disabled.")

#             refresh = self.get_token(user)
#             data = {
#                 'email': user.email,
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
#             return data

#         else:
#             raise serializers.ValidationError("Must include 'email' and 'password'.")


# class CustomTokenObtainSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         credentials = {
#             'email': attrs.get('email'),
#             'password': attrs.get('password')
#         }

#         if all(credentials.values()):
#             user = authenticate(**credentials)
#             if user:
#                 return super().validate(attrs)
#             else:
#                 raise serializers.ValidationError("Unable to log in with provided credentials.")
#         else:
#             raise serializers.ValidationError("Must include 'email' and 'password'.")


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # Customize token claims if needed
#         return token
