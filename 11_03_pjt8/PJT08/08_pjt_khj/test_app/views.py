from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import csv
import numpy as np
import pandas as pd

array_length = 1000
random_range = 5000


def file_open_by_numpy():
    np_arr = pd.read_csv('data/test_data.CSV', sep=",", encoding='cp949')
    return np_arr

@api_view(['GET'])
def p1(request):
    data = file_open_by_numpy()
    df = pd.DataFrame(data)
    data = df.to_dict('records')
    return JsonResponse({ 'dat': data})

@api_view(['GET'])
def p2(request):
    data = file_open_by_numpy()
    df = pd.DataFrame(data)
    data2 = df.to_dict('records')
    df.replace('', np.nan, inplace=True)
    df.fillna('NULL', inplace=True)
    data3 = df.to_dict('records')
    return JsonResponse({ 'dat': data3})

# def file_open_by_numpy2():
#     np_arr = pd.read_csv('data/test_data.CSV', sep=",", encoding='cp949')
#     return np_arr


@api_view(['GET'])
def p3(request):
    data = file_open_by_numpy()
    df = pd.DataFrame(data)
    df.replace('', np.nan, inplace=True)
    # df.replace('NULL', np.nan, inplace=True)

    df['diff'] = abs(df['나이'] - df['나이'].mean())

    # '나이차' 열을 정렬하고 상위 10개 값을 선택
    sorted_values = df.sort_values(by=['diff', '이름']).head(10)

    # 선택된 상위 10개의 값을 JSON으로 변환하여 반환
    top_10_records = sorted_values.to_dict('records')

    return JsonResponse({ 'dat': top_10_records })




# def file_open_by_pandas():
#     df = pd.read_csv('data/test_data.CSV', encoding='cp949')
#     return df.to_json(orient='records', force_ascii=False)

# @api_view(['GET'])
# def open(request):
#     data = file_open_by_pandas()
#     return JsonResponse(data, safe=False)


@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)
