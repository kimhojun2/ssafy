# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [0] *(N+1)
#     for _ in range(N):
#         arr = list(input().split())
#         tree[int(arr[0])] = arr[1
#
#
'''
우선순위 큐 : 데이터를 우선순위를 가지고 저장, 우선순위가 높은 것부터 꺼냄
힙 : 우선순위 큐를 구현하는 트리 기반의 자료구조, 최대힙, 최소 힙
import heapq
heapq.heappush(heap, num) : num을 최소 힙 heap에 삽입
heapq.heappop(heap) : 최소 힙 heap에서 가장 작은 값을 꺼내서 반환
'''