from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, PostSerializer, ReelSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from . models import User, Post, Reel
from . response import CustomResponse

# Create your views here.

class UserRegistration(APIView):

    def post(self, request, format=None):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse("Account Created Successfully", {} , status.HTTP_200_OK)
        else:
            return CustomResponse("Something Went Wrong", {serializer.errors}, status.HTTP_400_BAD_REQUEST)
    

class UserLogin(APIView):

    def post(self, request, format=None):
        data = request.data
        print(data)
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            print(serializer.data)
            user  = authenticate(email=serializer.data['email'],password=serializer.data['password'])
            if user:
                print(user)
                token,_ = Token.objects.get_or_create(user=user)
                
                return CustomResponse("Login Successful", {"token": str(token)} , status.HTTP_200_OK)
            else:
                return CustomResponse("Invalid Creds", {} , status.HTTP_403_FORBIDDEN)
        return CustomResponse("Something went wrong", {"errors": serializer.errors} , status.HTTP_400_BAD_REQUEST)


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.filter(id=request.user.id).first()
        print(user)
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
       


class PostView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        try:
            posts = Post.objects.all().order_by('-id')
            serializer  = PostSerializer(posts, many=True)
            return CustomResponse("Post", serializer.data , status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return CustomResponse("Error While fetching Post", {} , status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request, format=None):
        try:
            print(request.data)
            serializer  = PostSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse("Post Created", {} , status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return CustomResponse("Error in  Post Creation", {} , status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(e)
            return CustomResponse("Error in  Post Creation", {} , status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ReelView(APIView):
    def get(self, request, format=None):
        try:
            posts = Reel.objects.all().order_by('-id')
            serializer  = ReelSerializer(posts, many=True)
            return CustomResponse("Reel", serializer.data , status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return CustomResponse("Error While fetching Reel", {} , status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request, format=None):
        try:
            print(request.data)
            serializer  = ReelSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse("Reel Created", {} , status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return CustomResponse("Error in  Reel Creation", {} , status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(e)
            return CustomResponse("Error in Reel Creation", {} , status.HTTP_500_INTERNAL_SERVER_ERROR)
