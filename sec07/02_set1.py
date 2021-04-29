# 집합 (set)
# 수학의 집합
# 중복되지 않은 항목들이 모인 것
# 집합 = {항목1, 항목2, ..., 항목n}

# 집합의 특징
# 순서가 없다. : 입력/출력되는 순서가 다를 수 있음
# 동일한 요소(값)이 중복될 수 없다.
# 인덱스 사용 불가
# 요소 추가/삭제는 가능하지만 이미 포함되어 있는 요소(값)를 변경할 수는 없음
# 집합 안에 변경 가능한 항목을 포함할 수 없음
# - 리스트는 포함할 수 없음
# - 튜플은 포함 가능

# 집합 만들기
s1 = {1, 2, 3, 4, 5}
print(s1)
print(type(s1))  # <class 'set'>


# set() 함수 사용해서 집합 만들기
# 리스트로 집합 생성
s2 = set([10, 20, 30])
print(s2)

s3 = set((100, 200, 300))
print(s3)


# 동일한 요소(값)이 중복될 수 없다.
s4 = {1, 2, 3, 4, 3}  # 중복된 요소가 있어도 오류는 없음
print(s4)  # {1, 2, 3, 4} : 중복값을 제거하고 집합 생성


# 집합 안에 변경 가능한 요소(리스트) 포함할 수 없음
s5 = {1, 2, [3, 4]}
# TypeError: unhashable type: 'list'


# 인덱스 사용 불가
s4[0] = 100  # 오류 발생
# TypeError: 'set' object does not support item assignment


# 집합에 요소 추가
# add() 함수 사용 : 요소 1개 추가 시 사용
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

s.add(5, 6)  # 오류 발생 : 인수 1개만 가능
# TypeError: set.add() takes exactly one argument (2 given)


# update() : 요소를 여러 개 추가 시 사용
s.update([5, 6])
print(s)  # {1, 2, 3, 4, 5, 6}


# 합집합 : A | B, A.union(B)
# 교집합 : A & B, A.intersection(B)
# 차집합 : A - B, A.difference(B)

# 집합 연산
A = {1, 2, 3}
B = {3, 4, 5}

# 합집합
C = A | B
print(C)  # {1, 2, 3, 4, 5}

C = A.union(B)
print(C)  # {1, 2, 3, 4, 5}


# 교집합
C = A & B
print(C)  # {3}

C = A.intersection(B)
print(C)  # {3}


# 차집합
C = A - B
print(C)  # {1, 2}

C = A.difference(B)
print(C)  # {1, 2}