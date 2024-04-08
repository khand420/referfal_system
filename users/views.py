# users/views.py

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework_simplejwt.views import TokenObtainPairView
# from .serializers import MyTokenObtainPairSerializer
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import CustomTokenObtainSerializer

class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer




@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        # Extract and handle password field separately
        password = request.data.get('password')
        serializer.validated_data['password'] = password

        # Save the user using the updated serializer
        user = serializer.save()

        return Response({
            'user_id': user.id,
            'message': 'User registered successfully',
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def referrals(request):
    user = request.user
    referrals = User.objects.filter(referral_code=user.referral_code)
    
    # Pagination
    page = request.query_params.get('page', 1)
    paginator = Paginator(referrals, 20)
    
    try:
        referrals_page = paginator.page(page)
    except PageNotAnInteger:
        referrals_page = paginator.page(1) 
    except EmptyPage:
        referrals_page = paginator.page(paginator.num_pages)
    
    serializer = UserSerializer(referrals_page, many=True)
    return Response(serializer.data)













# @api_view(['POST'])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
    
#     if serializer.is_valid():
#         # Extract validated data from serializer
#         name = serializer.validated_data['name']
#         email = serializer.validated_data['email']
#         password = serializer.validated_data['password']
#         referral_code = serializer.validated_data.get('referral_code', None)

#         # Create a new user instance
#         user = User.objects.create_user(email=email, name=name, password=password, referral_code=referral_code)

#         # Return response with user details
#         return Response({
#             'user_id': user.id,
#             'message': 'User registered successfully',
#         }, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['POST'])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     print('serializer',serializer )
#     if serializer.is_valid():
#         user = serializer.save()
#         print(user)
#         # refresh = RefreshToken.for_user(user)
#         return Response({
#             'user_id': user.id,
#             'message': 'User registered successfully',
#             # 'access_token': str(refresh.access_token),
#         }, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         return Response({'user_id': user.id, 'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# token_obtain_pair_view = MyTokenObtainPairView.as_view()


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # Customize token claims if needed
#         # token['custom_claim'] = user.custom_field
#         return token

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# token_obtain_pair_view = CustomTokenObtainPairView.as_view()





# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import User
# from .serializers import UserSerializer

# @api_view(['POST'])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         referral_code = request.data.get('referral_code')
#         if referral_code:
#             referred_by_user = User.objects.filter(referral_code=referral_code).first()
#             if referred_by_user:
#                 # Award point to referring user
#                 referred_by_user.points += 1
#                 referred_by_user.save()
#         return Response({'user_id': user.id, 'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def user_details(request):
#     user = request.user
#     serializer = UserSerializer(user)
#     return Response(serializer.data)


# @api_view(['GET'])
# def user_referrals(request):
#     user = request.user
#     referrals = User.objects.filter(referral_code=user.referral_code).order_by('-registration_timestamp')
    
#     # Pagination
#     page = request.query_params.get('page', 1)
#     paginator = Paginator(referrals, 20)
#     try:
#         referrals = paginator.page(page)
#     except PageNotAnInteger:
#         referrals = paginator.page(1)
#     except EmptyPage:
#         referrals = paginator.page(paginator.num_pages)
    
#     serializer = UserSerializer(referrals, many=True)
#     return Response(serializer.data)
