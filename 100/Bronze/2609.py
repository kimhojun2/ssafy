a, b = map(int, input().split())

for i in range(min(a,b),0,-1):
    if a%i == 0 and b%i==0:
        print(i)
        print((a*b)//i)
        break



# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# a, b = map(int, input().split())
#
# print(gcd(a, b))
# print(lcm(a, b))
