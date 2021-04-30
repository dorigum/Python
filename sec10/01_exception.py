# Error
# - 문법적 오류나 실행 시간에 잘못된 메모리 접근 오류, 논리 오류, 사용자의 잘못된 입력 오류 등
# 예외 (Exception)
# - 오류에 대처하기 위한 오류
# - 주로 실행 중에 발생
# 예외 처리
# - 오류 발생 시 프로그램이 중단되고 에러 메시지가 출력되지 않도록
# - 예외를 발생시켜서 예외 처리를 통해 정상 실행되도록 하기 위한 방법

# 파이썬에서의 예외 처리 방법
# - try ... except 문 사용
# - 형식
# try:
#     예외 발생 가능 문장
# except 예외 유형:
#     예외 처리 문장
# else:
#     예외 없을 때 수행되는 문장
# finally:
#     예외 유무와 상관없이 항상 실행되는 문장

# 예외 처리 : 에러 확인
# ZeroDivisionError
print(10/0)  # ZeroDivisionError: division by zero

# TypeError
print("나이 : " + 23 + "살")
# TypeError: can only concatenate str (not "int") to str

# NameError
# print(b)
# NameError: name 'b' is not defined

# ValueError
c = 100
print("%d%" % c)  # ValueError: incomplete format

# SyntaxError
# if x > 10
#     print("홍길동")  # SyntaxError: invalid syntax

# IndexError
a = [1, 2, 3, 4]
print(a[5])
# IndexError: list index out of range


def add():
    a = a + 1  # Unresolved reference 'a'

# ModuleNotFoundError
# import mymodule
# ModuleNotFoundError: No module named 'mymodule'

# FileNotFoundError
f = open("exception.txt", 'r')
data = f.read()
print(data)
# FileNotFoundError: [Errno 2] No such file or directory: 'exception.txt'
