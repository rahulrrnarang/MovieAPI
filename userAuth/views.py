from django.shortcuts import render

from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from userAuth.models import Counter, User
from userAuth.generate_token import get_tokens_for_user


class RegisterUser(APIView):
    """Register new user."""
    def post(self, request):
        """Create new user and return token as response."""
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            raise ValidationError(f'User with {username} username alreay exists.')
        
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

        return Response(
            data=get_tokens_for_user(user),
            status=status.HTTP_201_CREATED
        )


class RequestCounter(APIView):
    """Views for request counter."""
    def get(self, request):
        counter = Counter.objects.get(key='request_count')
        
        return Response(data={'requests':counter.value})


class ResetRequestCounter(APIView):
    """View to reset request counter."""
    def post(self, request):

        counter = Counter.objects.get(key='request_count')
        counter.value = 0
        counter.save()

        return Response(data={'message':'request count reset successfully'})
