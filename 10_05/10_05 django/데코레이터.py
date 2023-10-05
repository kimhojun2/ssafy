# 데코레이터 함수
# 메인 로직(func 함수)을 감싸주는 새로운 함수를 만든다.
is_logined = False
def my_decorator(func):
    def wrapper():
        print("전처리")
        func()
        print("후처리")
    
    return wrapper

@my_decorator
def my():
    print("수행 내용")

my()