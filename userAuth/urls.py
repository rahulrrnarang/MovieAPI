from django.urls import path

from userAuth.views import RequestCounter, ResetRequestCounter

urlpatterns = [
    path('', RequestCounter.as_view(), name='get-request-count'),
    path('reset/', ResetRequestCounter.as_view(), name='reset-counter')
]

