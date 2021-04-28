# 동전 교환 프로그램
# 입력한 값을 모두 동전으로 교환
# 동전의 개수는 최소가 되게 함

# 교환할 돈은 얼마입니까? 7777 (입력 받음)
# 오백원 짜리 : 개
# 백원 짜리 : 개
# 오십원 짜리 : 개
# 십원 짜리 : 개
# 바꾸지 못한 잔돈 : 원
money = int(input("교환할 돈은 얼마입니까? : "))

coin500 = money // 500      # 나누기 몫 (500원 짜리)
money %= 500                # 500으로 나눈 나머지

coin100 = money // 100
money %= 100

coin50 = money // 50
money %= 50

coin10 = money // 10
money %= 10

print("\n오백원 짜리 : %d 개" % coin500)
print("백원 짜리 : %d 개" % coin100)
print("오십원 짜리 : %d 개" % coin50)
print("십원 짜리 : %d 개" % coin10)
print("바꾸지 못한 잔돈 : %d 원" % money)