# 파이썬 집합적 자료형
# 리스트 / 튜플 / 집합 / 딕셔너리

# 리스트 (list)
# 동일한 이름을 갖는 원소들의 연속 저장 영역
# 여러 개의 데이터가 저장되어 있는 장소 (집합적 자료형)
# 각 원소는 인덱스 (index)로 구분 (인덱스는 0부터 시작)
# 원소(값) 변경 가능
# 대괄호 [] 사용
# 리스트 = [값1, 값2, ...]
# scores = [90, 67, 88, 100]

# 리스트의 특징
# - 크기가 가변적
# - 다양한 종류의 데이터를 하나의 리스트 안에 저장 가능
# myList = [10, "dog", 180.3, "홍길동"]


names = ["홍길동", "이몽룡", "성춘향", "변학도"]
print(names)

# 리스트의 각 원소 출력
for name in names:
    print(name, end=" ")

# range() 함수 사용
for i in range(0, len(names)):
    print(names[i], end=" ")


# 리스트 안에 리스트 포함
numbers = [100, 200, 300, [10, 20, 30]]
for i in range(0, len(numbers)):
    print(numbers[i])


# 리스트의 각 원소의 값을 각 변수에 저장
a, b, c, d = numbers
print(a)
print(b)
print(c)
print(d)


# 특정 원소에 접근 : 인덱싱 (indexing)
# 리스트에서 인덱스 연산자를 통하여 요소를 참조하는 것
# b = [1, 2, 3, [10, 20]]
# b[4][0] : 10
# b[-1][1] : 20

b = [1, 2, 3, [10, 20]]
print(b[-1][1])  # 마지막 요소의 두번째 요소 20 출력


# 슬라이싱 : 리스트 안에서 범위를 지정하여 원하는 요소들을 선택하는 연산
# 리스트 주요 메소드
# len() / count()
# append() / insert()
# remove() / pop()
# extend()
# sort() / reverse()
# index()
# min() / max()

a = [1, 2, 3, 3, 4]
print("요소의 개수 : ", len(a))
print("3의 개수 : ", a.count(3))


# append() : 리스트의 끝에 새로운 요소 추가
# 리스트.append()
# insert() : 리스트의 특정 위치에 요소 삽입
# 리스트.insert(위치, 값)

a = [1, 2, 3, 3, 4]
a.append(5) # [1, 2, 3, 3, 4, 5]
print(a)

a.append([6, 7])  # 마지막에 하위 리스트 추가
print(a) # [1, 2, 3, 3, 4, 5, [6, 7]]

a.append(8, 9)  # 요소를 2개 이상 추가하면 오류 발생


# 빈 리스트 생성하고 요소 나중에 추가
valList = []
valList.append(10)
valList.append(20)
valList.append(30)
print(valList)


# for 문 사용하여 요소 추가
scores = []
for i in range(5):
    scores.append(i)

for score in scores:
    print(score)
    
    
# insert(위치, 값) : 리스트의 특정 위치에 요소 삽입
nums = [1, 2, 3, 4, 5]
nums.insert(1, 200) # 두번째 위치에 삽입
print(nums)  # [1, 200, 2, 3, 4, 5]

nums.insert(len(nums), 12.3) # 맨 뒤에 삽입
print(nums)  # [1, 200, 2, 3, 4, 5, 12.3]

nums.insert(-1, "홍길동") # 마지막 요소 앞에 삽입
print(nums)  # [1, 200, 2, 3, 4, 5, '홍길동', 12.3]

nums.insert(len(nums) -1, [10, 20]) # 마지막 요소 앞에 하위 리스트 추가
print(nums)  # [1, 200, 2, 3, 4, 5, '홍길동', [10, 20], 12.3]

