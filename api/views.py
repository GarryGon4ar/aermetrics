# Create your views here.

import pandas as pd
from django.db import transaction
from django.db.models import Sum
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Logs
from api.serializers import LogsSerializer, LogsFileUploadSerializer
from django_filters.rest_framework import DjangoFilterBackend


class LogsAPIView(generics.ListAPIView):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer


class LogsFileUploadView(generics.CreateAPIView):
    serializer_class = LogsFileUploadSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        Logs.objects.bulk_create(
            Logs(**row) for _, row in reader.iterrows()
        )

        return Response({"status": "success"}, status.HTTP_201_CREATED)


class AircraftsListView(APIView):
    """View all aircrafts."""

    def get(self, request):
        """Return a list of all aircrafts."""
        return Response(Logs.objects.values_list('aircraft').distinct().order_by('aircraft'))


class StatusesListView(APIView):
    """View all statuses."""

    def get(self, request):
        """Get a list of all statuses."""
        return Response(Logs.objects.values_list('status').distinct().order_by('status'))


class TypesListView(APIView):
    """View all types."""

    def get(self, request):
        """Get a list of all types."""
        return Response(Logs.objects.values_list('type').distinct().order_by('type'))


class MyGenericView(GenericAPIView):
    queryset = Logs.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status", "title", "type"]

    def get(self, request):
        queryset = self.get_queryset()
        if status_ := request.query_params.get('status'):
            queryset = queryset.filter(status=status_)
        if type_ := request.query_params.get('type'):
            queryset = queryset.filter(type=type_)
        if aircraft := request.query_params.get('aircraft'):
            queryset = queryset.filter(aircraft=aircraft)
        aggregate = queryset.aggregate(
            info_count=Sum('info_count'),
            errors_count=Sum('errors_count'),
            pre_legend=Sum('pre_legend'),
            warning=Sum('warning'),
            paired_b=Sum('paired_b'),
            legend=Sum('legend'),
            lower_b=Sum('lower_b'),
            repeat_legend=Sum('repeat_legend'),
            upper_a=Sum('upper_a'),
            lower_a=Sum('lower_a'),
            paired_a=Sum('paired_a'),
        )
        return Response(
            {
                "aircraft": self.request.query_params.get('aircraft'),
                "type": self.request.query_params.get('type'),
                "status": self.request.query_params.get('status'),
                "info_count": aggregate['info_count'],
                "errors_count": aggregate['errors_count'],
                "pre_legend": aggregate['pre_legend'],
                "warning": aggregate['warning'],
                "paired_b": aggregate['paired_b'],
                "legend": aggregate['legend'],
                "lower_b": aggregate['lower_b'],
                "repeat_legend": aggregate['repeat_legend'],
                "upper_a": aggregate['upper_a'],
                "lower_a": aggregate['lower_a'],
                "paired_a": aggregate['paired_a'],
            }
        )
