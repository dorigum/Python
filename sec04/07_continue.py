# continue 문
# 반복 수행 중에 continue 문을 만나면
# 현재 시점에서 중단하고
# 다음 반복을 계속 수행

x = 0
while x < 10:
    x += 1
    if x % 2 == 0:  # 짝수이면
        continue

    print(x)    # 반복 수행되는 문장 (continue 때는 수행되지 않음)
