from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics ,status
from rest_framework.authtoken.models import Token
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
