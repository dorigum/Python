# 데이터 타입
# 정수 : int
# 실수 : float
# 문자열 : str
# 불리언 : bool

# 변수의 데이터 타입
# - 파이썬에서는 변수는 지정된 자료형이 없음
# - 저장한 값에 따라 변수의 자료형이 정해짐
# - 한 변수에 정수값을 저장하면 int 형이 되고
# - 문자열 값을 저장하면 str 형이 됨
a = 100
print(type(a))

a = "hello"
print(type(a))

# 형 변환 함수
# int(문자열) : 문자열을 정수로 변환
# float(문자열) : 문자열을 실수로 변환
# str(정수 또는 실수) : 정수 또는 실수를 문자열로 변환

# input() 함수 : 콘솔에서 입력 가능 (입력된 값은 문자열)
num = input("숫자 입력 : ")
print(num)

print(type(num))

# 입력된 값을 숫자 연산
# 입력된 값은 문자열이므로 숫자 연산 불가 -> 숫자로 형 변환 필요
print(int(num) + 100)
print(type(num))

# 이름, 나이 입력 받아서 출력
# 이름 : 홍길동, 나이 : 23
name = input("이름 입력 : ")
age = input("나이 입력 : ")

print("이름 : " + name + ", 나이 : " + age)

# eval() : 숫자로 변환 함수 (숫자 입력 및 수식 입력 가능)
x = eval(input("숫자 입력 1 : "))
y = eval(input("숫자 입력 2 : "))
sum = x + y
print("합 : ", sum)

# 연습문제
# 예금액과 이자율 입력 받아서
# 예금액, 이자율, 예금이자, 잔액 출력

# 실행 예
# 예금액 입력 : 10000
# 이자율 입력(%) : 2.5
# --------------------------
# 예금액 : 10000원
# 이자율 : 2.5%
# 예금이자 : 250원 (계산해서 출력)
# 잔액 : 10250원 (계산해서 출력)

deposit = int(input("예금액 입력 : "))
intRate = float(input("이자율 입력(%) : "))

interest = int(deposit * intRate / 100)
balance = deposit + interest

print("----------------------------")
print("예금액 : %d 원" % deposit)
print("이자율 : %.1f %%" % intRate)
print("예금이자 : %d 원" % interest)
print("잔액 : %d 원" % balance)

# 숫자에서 천 단위 구분(,) 기호 출력 : format() 함수 사용
# 숫자에 , 붙임 : 더 이상 숫자가 아니고 문자가 됨 (%s)
# format() 함수와 포맷 코드 같이 사용
print("예금액 : %s 원" % format(deposit, ','))
print("이자율 : %.1f %%" % intRate)
print("예금이자 : %s 원" % format(interest, ','))
print("잔액 : %s 원" % format(balance, ','))

# 포맷 코드 사용하지 않고 format() 함수 사용 가능
print("예금액 : ", format(deposit, ','), " 원")
print("이자율 : %.1f %%" % intRate)
print("예금이자 : ", format(interest, ','), " 원")
print("잔액 : 원", format(balance, ','), " 원")
