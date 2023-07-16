import requests
import os

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

class MayaMovieApi(APIView):
    """Third party movie API integration."""
    def get(self, request):
        requests.get()
        