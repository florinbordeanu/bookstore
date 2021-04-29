from django.urls import path
from accounts.views import signup, search_books, ChangePassword
from django.contrib.auth import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('search', search_books, name='search_books'),
    path('reset_password/', PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
         name='reset_password'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),
]