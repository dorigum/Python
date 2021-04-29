# 1. temp 이름의 빈 딕셔너리 생성

# 2. 아이스크림의 이름, 희망가격을 딕셔너리로 구성 : icecream
# 이름      희망가격
# 메로나      1000
# 폴라포      1200
# 빵빠레      1800

# 3. icecream 딕셔너리에 항목 추가
# 죠스바 1200
# 월드콘 1500

# 4. icecream 딕셔너리에서 메로나 가격 출력
# 메로나 가격 : 1000

# 5. icecream 딕셔너리에서 메로나 가격을 1300으로 수정

# 6. icecream 딕셔너리에서 가격 정보만 추출해서 출력


# 1. temp 이름의 빈 딕셔너리 생성
temp = {}


# 2. 아이스크림의 이름, 희망가격을 딕셔너리로 구성 : icecream
icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(icecream)

# 3. icecream 딕셔너리에 항목 추가
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print(icecream)


# 4. icecream 딕셔너리에서 메로나 가격 출력
print("메로나 가격 : ", icecream["메로나"])


# 5. icecream 딕셔너리에서 메로나 가격을 1300으로 수정
icecream["메로나"] = 1300
print("메로나 가격 : ", icecream["메로나"])


# 6. icecream 딕셔너리에서 가격 정보만 추출해서 출력 : values()
for value in icecream.values():
    print(value, end=" ")


print(sum(icecream.values()))
