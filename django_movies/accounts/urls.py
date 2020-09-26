from django.contrib.auth.views import LoginView
from django.urls import path
from accounts.views import SubmittableLoginView, SuccessMessagedLogoutView, SubmittablePasswordChangeView


app_name = 'accounts'

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', SuccessMessagedLogoutView.as_view(), name='logout'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password'),
]