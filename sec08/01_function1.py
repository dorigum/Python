# 함수 (function) : 특정 작업을 수행하는 코드 집합
# 함수의 종류
# 내장 함수
# - 파이썬에 이미 만들어져 있는 함수들
# - 형식에 맞춰 함수 이름 호출해서 사용
# - print(), len(), input(), type(), sorted(), ...

# 사용자 정의 함수
# - 사용자가 임의로 만들어서 사용하는 함수

# 함수 구조
# def 함수명(매개변수1, 매개변수2):
#     수행 문장
#     return 반환값(생략 가능)

# 함수 이름
# - 함수의 목적을 설명하는 동사
# - 동사 + 명사
# compute_average()
# showResult()

# 함수 사용
# - 함수를 사용하려면 함수를 호출(call)해야 함
# - 함수 호출 : 함수 이름을 적는다.


# 매개변수 / 반환값이 없는 함수
def show_hello():
    print("hello")

show_hello()  # 함수 호출


# 반환 값이 있는 함수
# 함수의 반환 값 : 함수가 특정 기능을 수행하고 돌려주는 결과값
# return 문 사용
# 함수가 호출한 곳으로 반환

# 반환 값이 있는 함수
def sum():
    num1 = int(input("숫자1 입력 : "))
    num2 = int(input("숫자2 입력 : "))
    return num1 + num2  # 결과값 반환

# 함수를 호출하고 함수의 결과값 받기
# (1) 변수에 저장해서 사용
total = sum()
print("합 : %d" % total)  # 합 : 30

# (2) 반환값을 직접 출력
print("합 : %d" % sum())


# 여러 개의 값 반환
# 파이썬을 제외한 다른 프로그래밍 언어에서는
# 함수는 항상 하나의 값만 반환 (return 문에 값이 1개)
# 파이썬에서는 함수가 여러 개의 값을 반환할 수 있음

def multi_return():
    return 1, 2, 3

# 반환된 여러 개의 값을 각 변수에 저장
a, b, c = multi_return()
print(a, b, c)  # 1 2 3

# 반환된 여러 개의 값을 하나의 변수로 받기
result = multi_return()  # 변수는 튜플로 만들어짐
print(result)  # (1, 2, 3)