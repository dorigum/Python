result = 10
print(result)

result = "abcd"
print(result)

# 여러 개의 변수에 여러 개의 값 저장
a, b, c, d = 1, 2, 3, 4
print(a)
print(b)
print(c)
print(d)

# 두 변수의 값 교환
# 변수1, 변수2 = 변수2, 변수1
a, b = 10, 20
print(a, b)
# 두 변수의 값 교환
a, b = b, a
print(a, b)

# 변수 삭제
# del 명령어 사용
# del 변수
del a
print(a) # NameError: name 'a' is not defined
