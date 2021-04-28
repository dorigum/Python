# 조건이 여러 개인 경우
# if (조건식1):
#     조건식1이 참인 경우 수행되는 문장
# elif (조건식2):
#     조건식2가 참일 경우 수행되는 문장
# else:
#     모든 조건식이 거짓일 경우 수행되는 문장

num = int(input("정수 입력 : "))

if num < 0:
    result = "음수"
elif num > 0:
    result = "양수"
else:
    result = "0"

print(result)