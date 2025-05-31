from django.urls import path
from users.views import (
    RegistrationView,
    LoginView,
    ProfileView,
    PasswordChangeView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
