# for 문 : 정해진 횟수만큼 반복
# for 문 형식
#
# for 변수 in 범위 또는 리스트:
#     반복 수행되는 문장



# for name in ["홍길동", "이몽룡", "성춘향", "변학도"]:
#     print(name)

# 홍길동 이몽룡 성춘향 변학도 : 옆으로 출력
for name in ["홍길동", "이몽룡", "성춘향", "변학도"]:
    print(name, end=" ")

for i in range(0, 10):
    print(i)


# range() 함수 : 특정 범위의 정수 생성
# range(10) : 0 ~ 9까지의 정수 10개 (시작은 0부터)
# range(start, stop) : start ~ stop-1
# - range(0, 10) : 0 ~ 9
# range(start, stop, step) : start에서 stop-1까지 step 간격으로 정수 생성
# - range(0, 10, 2) : 0 ~ 9까지 2씩 건너뛰면서 10보다 작은 정수

for i in range(11, 21):
    print(i, end=" ")

# 1 ~ 10 숫자 중에서 홀수만 출력
for i in range(1, 10, 2):
    print(i, end=" ")

# 1 ~ 100까지의 합 구하기
# 누적 변수 sumX : 반드시 초기화하고 사용해야 함
sumX = 0
for x in range(1, 101):
    sumX += x

print("1 ~ 100까지의 합 : ", sumX)


# 카운트다운 프로그램 작성
# 시작 숫자를 입력하시오 : 5
# 5 4 3 2 1 발사!

# 시작 숫자를 입력하시오 : 10
# 10 9 8 7 6 5 4 3 2 1 발사!
count = int(input("시작 숫자를 입력하시오 : "))
for x in range(count, 0, -1):
    print(x, end=" ")

print("발사!")