from django.shortcuts import render
from .serializers import RegisterSerializer,ChangePasswordSerializer,ChangeUsernameSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics ,status
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your views here.


@api_view(['POST', ])
def registration_views(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        dataa = {}

        if serializer.is_valid():
            user = serializer.save()

            dataa['response'] = 'Registration Successfully'
            dataa['username'] = user.username
            dataa['email'] = user.email

        else:
            dataa = serializer.errors

        return Response(dataa, status=status.HTTP_201_CREATED)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangeUsernameView(generics.UpdateAPIView):
    serializer_class = ChangeUsernameSerializers
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        user = User.objects.get(username=self.request.user.username)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user.username = serializer.data.get("new_username")
            user.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'username updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)