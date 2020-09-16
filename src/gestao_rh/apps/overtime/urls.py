from django.urls import path
from .views import (
    OvertimeList, OvertimeUpdate,
    OvertimeCreate, OvertimeDelete,
    ReportCSV
)

urlpatterns = [
    path('', OvertimeList.as_view(), name='overtime-list'),
    path('new/', OvertimeCreate.as_view(), name='overtime-create'),
    path('edit/<int:pk>/', OvertimeUpdate.as_view(), name='overtime-update'),
    path('delete/<int:pk>/', OvertimeDelete.as_view(), name='overtime-delete'),
    path('report-csv/', ReportCSV.as_view(), name='overtime-report-csv'),
]
