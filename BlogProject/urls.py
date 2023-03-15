from django.contrib import admin
from django.urls import path , include
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('auth_user.urls')),
    path('swagger/', get_swagger_view(title='Post Api')),
]
