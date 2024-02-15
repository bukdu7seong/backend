import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CustomTokenObtainPairSerializer, Custom42TokenObtainPairSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
import requests


# Login View
class MyLoginView(ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='login')
    def login_account(self, request):
        username = request.data.get('username', None)
        try:
            user = User.objects.get(username=username)
            return self._get_user_token(request)
        except User.DoesNotExist:
            return Response('have to redirect to sign up', status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'], url_path='login/42')
    def login(self, request):
        code = request.query_params.get('code', None)
        if code is not None:
            response = self.get_42_access_token(code)
            if response.status_code == 200:
                email = self.get_42_email(response)
                try:
                    user = User.objects.get(email=email)
                    request.data['email'] = email
                    if user.twoFactor:
                        return Response({"twoFactor": True}, status=status.HTTP_301_MOVED_PERMANENTLY)
                    else:
                        return self._get_42_user_token(request)
                except User.DoesNotExist:
                    return Response(email, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response('fail to get 42 access token', status=400)
        else:
            return Response('fail to get code', status=400)

    def get_42_email(self, response):
        js = response.json()
        token = js.get('access_token')
        user_info = requests.get('https://api.intra.42.fr/v2/me', headers={'Authorization': 'Bearer ' + token})
        if user_info.status_code == 200:
            return user_info.json()['email']
        else:
            return None

    def get_42_access_token(self, code):
        data = {
            "grant_type": "authorization_code",
            "client_id": "u-s4t2ud-33518bf1e037b1706036053f6530503148e5995f22e2a5dca937497ee382c944",
            "client_secret": "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",
            "code": code,
            "redirect_uri": "http://127.0.0.1:8000/account",
        }
        try:
            return requests.post("https://api.intra.42.fr/oauth/token", data=data)
        except requests.exceptions.RequestException as e:
            return HttpResponse(str(e), status=500)

    def _get_user_token(self, request):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _get_42_user_token(self, request):
        serializer = Custom42TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # SignUp View
# class SignupView(APIView):
#     def post(self, request, format=None):

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("ok")


def check_signup(user_info):
    return False


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = User(title=title, content=content)
        user.save()
        return redirect('articles:index')
    else:
        return render(request, 'articles/create.html')


def get_42authorization(request):
    url = "https://api.intra.42.fr/oauth/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": "u-s4t2ud-33518bf1e037b1706036053f6530503148e5995f22e2a5dca937497ee382c944",
        "client_secret": "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",
        "scope": "public"
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return redirect("https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud"
                            "-33518bf1e037b1706036053f6530503148e5995f22e2a5dca937497ee382c944&redirect_uri=http%3A"
                            "%2F%2F127.0.0.1%3A8000%2Faccount&response_type=code")
        else:
            return HttpResponse(response.content, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=50)


def name(request):
    return HttpResponse("Hello, world. You're at the", status=200)


def signup(request):
    data = json.loads(request.body)
    user = User.objects.create_user(
        username=data.get('username'),
        email=data.get('email'),
        password=data.get('password'),
    )
    user.save()
    return HttpResponse("ok")
