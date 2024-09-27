from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('verify/', views.VerifyEmailView.as_view(), name='verify'),
    path('login/', views.SessionLoginAPIView.as_view(), name='session-login'),
    path('logout/', views.SessionLogoutAPIView.as_view(), name='session-logout'),
]