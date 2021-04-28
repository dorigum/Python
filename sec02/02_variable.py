# 문자열 사용 : 큰 따옴표, 작은 따옴표 사용 가능
name = "홍길동"
age = 23

print(name, age) # 변수 2개 옆으로 출력

address = '서울시 강남구 1번지' # 작은 따옴표 사용

print(name + "은 " + address + "에 삽니다.")
print(name + '은 ' + address + '에 삽니다.')

print(name + "은 " + age + "살 입니다.") # 정수형 변수를 문자열 연결 시 오류 발생

print(name + "은 " + str(age) + "살 입니다.") # 형 변환 필요
# 숫자를 문자열과 연결하기 위해서는
# 숫자를 문자열 타입으로 형 변환 필요 : str() 함수 사용
