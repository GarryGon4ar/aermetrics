# api/urls.py
from django.urls import path

from api.views import LogsAPIView, LogsFileUploadView

urlpatterns = [
    path('', LogsAPIView.as_view()),
    path('upload/', LogsFileUploadView.as_view(), name='upload-file'),
]
