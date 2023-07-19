from django.urls import path
from .views import *

urlpatterns = [
    path('',MayaMovieApi.as_view(), name='lala')
]
