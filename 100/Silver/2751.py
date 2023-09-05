import sys

input = sys.stdin.readline

n = int(input())
L = []
for i in range(n):
    a = int(input())
    L.append(a)
L.sort()

for i in range(len(L)):
    print(L[i])