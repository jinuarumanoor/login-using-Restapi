from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,UserLoginSerializer,UserprofileSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh['email'] = user.email
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class UserRegistrationview(APIView):

    def post(self, request, format=None):
        """
        Return a list of all users.
        
        """
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            print(user)
            return Response({'msg':'Registration Success'},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)


class UserLogin(APIView):

    def post(self, request , format=None):
        serializer= UserLoginSerializer(data= request.data)
        if serializer.is_valid(raise_exception = True):
            email = serializer.data['email']
            print(type(email))
            password = serializer.data['password']
            print(password)
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                # return Response({'msg':'Login Success'},status=status.HTTP_200_OK)
                token= get_tokens_for_user(user)
                
                return Response({'token':token , 'msg':'Login Successful'})

            else:
                return Response({'msg':'Login Failed'})


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
  
    def get(self, request, format=None):
        serializer= UserprofileSerializer(request.user)
        print(request.user)
        return Response(serializer.data)