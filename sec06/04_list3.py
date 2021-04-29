# 리스트 요소 정렬 : sort() / reverse() / sorted()
# sort() : 리스트 메소드
# 리스트의 요소를 정렬 (기본 : 오름차순)
# 원본 리스트 변경
# 리스트.sort()
# 내림차순 정렬 : sort(reverse = True)

# reversed()
# 역순으로 원본 리스트 변경 (정렬은 하지 않고 순서만 반대로)
# 리스트.reverse()

# sorted() : 파이썬 내장 함수
# 원본 리스트 유지하면서
# 정렬된 새로운 리스트 반환
# sorted(리스트)


# sort() : 리스트의 요소를 정렬 (기본 : 오름차순)
# 원본 리스트 변경
scores = [90, 78, 81, 64, 89]
scores.sort()  # 기본 : 오름차순
print(scores)  # [64, 78, 81, 89, 90] : 원본 리스트 변경됨

scores = [90, 78, 81, 64, 89]
scores.sort(reverse=True)   # 내림차순 정렬
print(scores)               # [90, 89, 81, 78, 64] : 원본 리스트 변경됨


# reversed() : 역순으로 원본 리스트 변경 (정렬은 하지 않고 순서만 반대로)
scores = [90, 78, 81, 64, 89]
scores.reverse()
print(scores)   # [89, 64, 81, 78, 90] : 역순으로 변경 (정렬은 안함)


# 영문자는 대문자가 앞으로, 소문자가 뒤로 정렬됨
# A : 65, a : 97
char = ['b', 'A', 'd', 'C']
char.sort()
print(char)     # ['A', 'C', 'b', 'd']


# 대소문자 구별 없이 정렬
# key 매개변수에 str.lower 지정
char = ['b', 'A', 'D', 'c']
char.sort(key=str.lower)
print(char)  # ['A', 'b', 'c', 'D']


# 대소문자 구별 없이 역순으로 정렬
char = ['b', 'A', 'D', 'c']
char.sort(key=str.lower, reverse=True)
print(char)  # ['D', 'c', 'b', 'A']


# sorted() : 원본 리스트 유지하면서 정렬된 새로운 리스트 반환
a = [3, 5, 2, 1, 4]
b = sorted(a)
print("a : ", a)  # a :  [3, 5, 2, 1, 4] : 원본 유지
print("b : ", b)  # b :  [1, 2, 3, 4, 5] : 새로운 리스트로 만들어짐


# max() / min()
# max() : 리스트 내에서 최대값 요소 반환
# min() : 리스트 내에서 최소값 요소 반환
n = [100, 7, -2, 99, 30]
print("최대 : ", max(n))  # 최대 :  100
print("최소 : ", min(n))  # 최소 :  -2


# 문자는 아스키 코드값으로 비교
c = ['c', 'a', 'D', 'A', 'b']
print("최대 : ", max(c))  # a: 97, b: 98, c: 99 : 최대(c)
print("최소 : ", min(c))  # A: 65 : 최소(A)


# index() : 리스트 안에서 요소의 위치 값 반환
# 요소가 존재하지 않으면 오류 발생
# 리스트.index(값)
# a = [1, 2, 3, 4, 5]
# a.index(3) : 값 3의 위치 (인덱스 값) 2 반환
# a.index(10) : 존재하지 않는 값은 오류 발생
names = ["홍길동", "이몽룡", "성춘향", "변학도"]
print(names.index("성춘향"))  # 위치 인덱스 2 : (세번째)
print(names.index("박지성"))  # ValueError: '박지성' is not in list


# 리스트에는 find() 메소드는 없음
# 문자열에서는 find()와 index() 모두 위치 값을 반환
# 차이점 : 못 찾으면 find()는 -1 반환, index()는 오류 발생
print(names.find("성춘향"))  # AttributeError: 'list' object has no attribute 'find'


# in / not in
# 리스트 내에서 요소의 존재 여부 반환 (True / False)
# in : 존재하면 True 반환
# not in : 존재하지 않으면 True 반환
num = [1, 2, 3, 4, 5]
result = 2 in num
print(result)  # True

result = 3 not in num
print(result)  # False
