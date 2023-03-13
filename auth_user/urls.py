from django.urls import path
from . import views
from rest_framework.authtoken import views as view

urlpatterns = [
    path('api-token-auth/', view.obtain_auth_token, name='api-token-auth'),
    path('register/',views.registration_views, name='register'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('change_username/', views.ChangeUsernameView.as_view(), name='change-username'),
]