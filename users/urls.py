from django.urls import path
from users.views import (
    RegistrationView,
    LoginView,
    ProfileView,
    PasswordChangeView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    ProfileUpdateView,
    AdminProfileUpdateView,
    AdminUserListView,
    UserRoleUpdateView,
)
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('admin-profile-update/<int:pk>/', AdminProfileUpdateView.as_view(), name='admin-profile-update'),
    path('admin-user-list/', AdminUserListView.as_view(), name='admin-user-list'),
    path('user-role-update/<int:pk>/', UserRoleUpdateView.as_view(), name='user-role-update'),
]
