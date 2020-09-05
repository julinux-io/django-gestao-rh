from django.urls import path
from .views import (
    DocumentsCreate, DocumentsDelete
)

urlpatterns = [
    path('new/<int:employment_id>/', DocumentsCreate.as_view(),
         name='documents-create'),
    path('delete/<int:pk>/', DocumentsDelete.as_view(), name='documents-delete'),
]
