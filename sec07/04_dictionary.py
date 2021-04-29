# 딕셔너리 (dictionary)
# - 키(key)와 값(value)의 한 쌍을 요소로 갖는 자료형
# - 딕셔너리 = {키1:값1, 키2:값2, ...}
# - d = {1:'a', 2:'b', 3:'c'}

# 딕셔너리의 특징
# - 순서가 없다. 따라서 인덱스로 접근할 수 없다.
# - key를 통해서만 접근 가능
# - key는 숫자, 문자 다 가능
# - key:value 한 쌍을 item 이라고 한다.
# - 쉼표(,)로 item을 구분
# - 중괄호 {} 사용

# 딕셔너리의 주요 함수
# - 딕셔너리변수.keys() : key만 추출해서 리스트로 반환 [1, 2, 3]
# - 딕셔너리변수.values() : value만 추출해서 리스트로 반환 : ['a', 'b', 'c']
# - 딕셔너리변수.items() : (key:value)의 튜플을 추출해서 리스트로 반환
#    - [(1:'a'), (2:'b'), (3:'c')]

# 딕셔너리 만드는 방법
# (1) {} 중괄호 안에 키 : 값 형식으로 저장
# (2) 빈 딕셔너리 만들어서 추가 : {} 만 지정
# (3) dict() 함수 사용


# (1) {} 중괄호 안에 키 : 값 형식으로 저장
scores = {'kor':90, 'eng':88, 'math':95}
print(scores)  # {'kor': 90, 'eng': 88, 'math': 95}


# (2) 빈 딕셔너리 만들어서 추가 : {} 만 지정
students = {}
students['name'] = '홍길동'  # key와 value 추가
students['age'] = 27
print(students)  # {'name': '홍길동', 'age': 27}


# (3) dict() 함수 사용
person = dict()
print(person)  # {}
# key와 value 추가
person["이름"] = "홍길동"
person["키"] = 175
person["몸무게"] = 78
print(person)  # {'이름': '홍길동', '키': 175, '몸무게': 78}

person2 = dict(이름='이몽룡', 키=175, 몸무게=88)
print(person2)  # {'이름': '이몽룡', '키': 175, '몸무게': 88}

# zip([키], [값])
person3 = dict(zip(['이름', '키', '몸무게'], ['성춘향', 160, 50]))
print(person3)  # {'이름': '성춘향', '키': 160, '몸무게': 50}


# 길면 여러 줄로 입력해도 됨
naver = {
    'name':'naver',
    'url':'www.naver.com',
    'userid':'nv',
    'password':'1234'
}

google = {
    'name':'google',
    'url':'www.google.com',
    'userid':'gg',
    'password':'5678'
}

print(naver)
print(google)


# keys(), values(), items()
print(naver.keys())
print(naver.values())
print(naver.items())

# keys(), values(), items() 함수가 반환한 값을 리스트로 변환해서 사용
# list() 함수 사용
to_list = list(naver.keys())
print(to_list)

# 각 요소 출력
for key in to_list:
    print(key)

# key만 추출
for key in naver.keys():
    print(key)

# value만 추출
for value in naver.values():
    print(value)

# item만 추출
for item in naver.items():
    print(item)

# key로 value 찾기
print(naver['userid'])  # nv
print(naver.get('password')) # 1234

# 존재하지 않을 경우
print(naver['link'])  # 오류 발생 : KeyError: 'link'
print(naver.get('link'))  # 오류없이 None 출력
print(naver.get('link', '없음'))  # '없음' 출력

# 존재하지 않을 경우 if 문으로 처리
insert_key = "link"
if naver.get(insert_key) is None:
    print(insert_key + "에 대한 데이터가 없습니다.")

# 존재 여부만 확인 : in / not in
print('link' in google)  # False
print('link' not in google)  # True

# 리스트의 메소드 확인
my_list = []
print(type(my_list))
print(dir(my_list))

# 튜플의 메소드 확인
my_tuple = ()
print(type(my_tuple))
print(dir(my_tuple))

# 딕셔너리 메소드 확인
my_dictionary = {}
print(type(my_dictionary))
print(dir(my_dictionary))
