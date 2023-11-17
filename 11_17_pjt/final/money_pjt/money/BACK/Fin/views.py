from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
import requests
from .models import DepositProducts, DepositOptions

API_KEY = settings.API_KEY

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    print(API_KEY)
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1"
    
    response = requests.get(url).json()
    
    for product in response['result']['baseList']:
        fin_prdt_cd = product.get('fin_prdt_cd')
        kor_co_nm = product.get('kor_co_nm')
        fin_prdt_nm = product.get('fin_prdt_nm')
        etc_note = product.get('etc_note')
        join_deny = product.get('join_deny')
        join_member = product.get('join_member')
        join_way = product.get('join_way')
        spcl_cnd = product.get('spcl_cnd')
        
        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd,
        }
        
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    for option in response['result']['optionList']:
        
        save_data = {
            'fin_prdt_cd': option.get('fin_prdt_cd'),
            'intr_rate_type_nm': option.get('intr_rate_type_nm'),
            'intr_rate': option.get('intr_rate') if option.get('intr_rate') else -1,
            'intr_rate2': option.get('intr_rate2'),
            'save_trm': option.get('save_trm'),
        }
    
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=DepositProducts.objects.get(fin_prdt_cd=option.get('fin_prdt_cd')))
    
    return JsonResponse({'message': 'okay'})


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        serializer = DepositProductsSerializer(DepositProducts.objects.all(), many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        fin_prdt_cd = request.data["fin_prdt_cd"]
        kor_co_nm = request.data["kor_co_nm"]
        fin_prdt_nm = request.data["fin_prdt_nm"]
        etc_note = request.data["etc_note"]
        join_deny = request.data["join_deny"]
        join_member = request.data["join_member"]
        join_way = request.data["join_way"]
        spcl_cnd = request.data["spcl_cnd"]
        
        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd,
        }
                
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
        return Response(serializer.data)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    serializer = DepositOptionsSerializer(DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd), many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    options = DepositOptions.objects.all()
    
    max_cd = -1
    max_rate = 0
    max_id = -1
    
    for option in options:
        if option.intr_rate2 > max_rate:
            max_rate = option.intr_rate2
            max_cd = option.fin_prdt_cd
    
    deposit_product = DepositProductsSerializer(DepositProducts.objects.filter(fin_prdt_cd=max_cd), many=True)
    options = DepositOptionsSerializer(DepositOptions.objects.filter(fin_prdt_cd = max_cd), many=True)
    
    return Response({'deposit_product': deposit_product.data[0], 'options': options.data})