from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
import requests
import json
# Create your views here.

@api_view(['GET'])
def exchange_rate(request):
    if request.method == 'GET':
        api_url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=r2L3MOeBhzmCs0W9Ismk0LcWtpageXlH&searchdate=20180102&data=AP01'

        response = requests.get(api_url)
        json_data = response.json()
        return Response(json_data)