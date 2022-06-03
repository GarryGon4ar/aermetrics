# api/urls.py
from django.urls import path

from api.views import LogsAPIView, LogsFileUploadView, AircraftsListView, StatusesListView, TypesListView, MyGenericView

urlpatterns = [
    path('', LogsAPIView.as_view()),
    path('upload/', LogsFileUploadView.as_view(), name='upload-file'),
    path('aircrafts/', AircraftsListView.as_view(), name='aircrafts'),
    path('statuses/', StatusesListView.as_view(), name='statuses'),
    path('types/', TypesListView.as_view(), name='statuses'),
    path('statistics/', MyGenericView.as_view(), name='statuses'),
]
