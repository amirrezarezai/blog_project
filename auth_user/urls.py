from django.urls import path
from . import views
from rest_framework.authtoken import views as view

urlpatterns = [
    path('api-token-auth/', view.obtain_auth_token, name='api-token-auth'),
    path('register/',views.registration_views),
]