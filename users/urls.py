
from django.urls import path
from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [   
    path('register/', views.register_user, name='register_user'),
    path('user-details/', views.user_details, name='user_details'),
    path('referrals/', views.referrals, name='referrals'),
    path('token/', views.CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    # path('token/', views.CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    # path('token/', views.token_obtain_pair_view, name='token_obtain_pair'),
     
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token creation
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh
]