from django.urls import path
from .views import OvertimeList

urlpatterns = [
    path('', OvertimeList.as_view(), name='overtime-list'),
]
