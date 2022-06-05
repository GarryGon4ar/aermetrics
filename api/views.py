# Create your views here.

import pandas as pd
from django.db import transaction
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Logs
from api.serializers import LogsFileUploadSerializer
from django.db import connection


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


class LogsAPIView(APIView):
    """View logs statistics view."""

    def get(self, request):
        """GET method with raw query."""
        query_ = '''
        SELECT 
            aircraft, 
            type, 
            status, 
            sum(info_count) as info_count, 
            sum(errors_count) as errors_count, 
            sum(pre_legend) as pre_legend, 
            sum(warning) as warning, 
            sum(paired_b) as paired_b, 
            sum(legend) as legend, 
            sum(lower_b) as lower_b, 
            sum(repeat_legend) as repeat_legend, 
            sum(upper_a) as upper_a, 
            sum(lower_a) as lower_a, 
            sum(paired_a) as paired_a  
        FROM api_logs 
        group by 
            grouping sets (
                (aircraft), (type), (status)
            ) 
        order by aircraft, type, status'''
        with connection.cursor() as c:
            c.execute(query_)
            columns = [col[0] for col in c.description]
            return Response(dict(zip(columns, row)) for row in c.fetchall())
