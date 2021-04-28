# 가위바위보 게임
# 홍길동 입력 : 바위 입력한 경우
# 이몽룡 입력 : 가위
# 홍길동이 이겼습니다.

# 홍길동 입력 : 바위 입력한 경우
# 이몽룡 입력 : 보
# 이몽룡이 이겼습니다.

# 홍길동 입력 : 가위 입력한 경우
# 이몽룡 입력 : 가위
# 비겼습니다.


# 방법1
# hong = input("홍길동 입력 : ")
# lee = input("이몽룡 입력 : ")
#
# # '홍길동' 이 이기는 모든 경우의 수
# if hong == '가위' and lee == '보' or \
#    hong == '바위' and lee == '가위' or \
#    hong == '보' and lee == '바위':
#     print("홍길동이 이겼습니다.")
# elif hong == lee:
#     print("비겼습니다.")
# else:
#     print("이몽룡이 이겼습니다.")


# 방법2
print("1: 가위, 2: 바위, 3: 보")
hong = int(input("홍길동 입력 : "))
lee = int(input("이몽룡 입력 : "))

# 홍길동이 이기는 모든 경우의 수
result = hong - lee
if result == 1 or result == -2:
    print("홍길동이 이겼습니다.")
elif result == 0:
    print("비겼습니다.")
else:
    print("이몽룡이 이겼습니다.")