# 7을 입력할 때까지 계속 입력하는 프로그램
# 7을 입력하면 프로그램 종료 (while 문 사용)

# 숫자 입력 : 3
# 다시 입력 : 9
# 다시 입력 : 1
# 다시 입력 : 7
# 7 입력했습니다. 종료.

num = int(input("숫자 입력 : "))

while num != 7:
    num = int(input("다시 입력 : "))

print(num, " 입력했습니다. 종료.")


# 무한 반복 : 조건을 True로 설정
# 반복문을 종료하기 위해 break 문 사용
while True:
    print("반복 수행되는 문장입니다.")
    answer = input("종료하려면 x 입력 :")
    if answer == 'x':
        break

print("종료했습니다.")