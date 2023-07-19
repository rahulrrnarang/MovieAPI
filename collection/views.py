from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import os

from rest_framework.views import APIView
from rest_framework.response import Response

class MayaMovieApi(APIView):
    """Third party movie API integration."""
    def __init__(self):
        """Initialize maya movie API."""
        load_dotenv('api_credentials.env')
        self.url = os.environ.get('API_URL')
        self.username = os.environ.get('API_USERNAME')
        self.password = os.environ.get('API_PASSWORD')

    def get(self, request):
        """Fetch movie list."""
        page = request.query_params.get('page')
        print(request.get_host(), 'rahul_narang')
        response = requests.get(
            self.url,
            auth=HTTPBasicAuth(self.username, self.password),
            params={'page':page} if page else None
        )
        return Response(response.json(), status=response.status_code)

