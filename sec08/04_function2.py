# 매개변수가 있는 함수
# 매개변수 (parameter) : 함수로 전달되는 값을 받는 변수
# 인수 (argument) : 함수를 호출하면서 함수에게 실제로 전달되는 값

def add(num1, num2):  # 매개변수
    print(num1 + num2)

add(10, 20)  # 인수(인자)


# 디폴트 매개변수 : 매개변수에 기본값 지정
def greet(name, msg="안녕^^"):
    print(name + ", " + msg)

greet("홍길동", "잘 지내요?")
greet("이몽룡")  # 디폴트 매개변수가 적용

# 주의!! 디폴트 매개변수는 마지막에 위치해야 함
# 앞에 올 경우 오류 발생
# def greet(msg="안녕^^", name):
#     print(name + ", " + msg)
# SyntaxError: non-default argument follows default argument

greet("이몽룡")


# 디폴트 매개변수 예제
def show_info(name, year=4, age=23):
    print(name, year, age)

show_info("홍길동")
show_info("이몽룡", 3)
show_info("성춘향", 1, 20)


# 가변길이 매개변수 (*args / **kwargs)
# - 1개의 매개변수로 개수가 정해지지 않은 여러 개의 값을 전달 받을 때 사용하는 매개변수
# - *args : arguments의 약자 (인수 값을 받음)
# - **kwargs : keyword arguments의 약자 (key=value 값을 받음)

# *args
# - def sum(*args):
# - sum(1, 2, 3)  # 인수가 3개
# - sum(1, 2, 3, 4, 5)  # 인수가 5개
# - *args 대신 다른 이름 사용 가능 : *names, *numbers, ...

# **kwargs
# - def info(**kwargs):
# - info(id="abcd", name="kim")  # 인수가 2개인 경우
# - info(id="abcd", name="lee", age=30)  # 인수가 3개


# 가변길이 매개변수 *args 예제
def show_players(*players):

    for player in players:
        print(player, end=" ")

    print()

show_players("손흥민", "박지성")
show_players("손흥민", "박지성", "황의조")


# 가변길이 매개변수 *args 예제
def order_coffee(coffee, *options):
    print(coffee + ", 옵션 : ", end=" ")

    for opt in options:
        print(opt, end=' ')

    print()

order_coffee("아메리카노", "Tall", "HOT", "시럽", "stay")
order_coffee("카페라떼", "Grande", "ICE", "go")


# 가변길이 매개변수 **kwargs 예제
def show_keywords(**kwargs):
    print("---------------------------------")
    for key in kwargs.keys():
        print(key, end=" ")

    print('\n')

    for value in kwargs.values():
        print(value, end=' ')

    print('\n')

    for item in kwargs.items():
        print(item)

show_keywords(id='sun',
              name='kim',
              phone='010-1234-1234')

show_keywords(id='moon',
              name='lee',
              phone='010-1111-1111',
              address='제주도 서귀포시')


# 위치 인수 vs 키워드 인수
# 위치 인수 (positional arguments) (일반적인 인수)
# - 함수 호출 시 위치에 의하여 구별하는 방식
# - 매개변수의 순서대로 인수를 전달해서 사용하는 경우
# - def add(a, b, c):
# - 호출 : add(10, 20, 30)


# 키워드 인수 (keyword arguments)
# - 인수들 앞에 키워드를 두어서 인수를 구별하는 방식
# - 인수의 위치가 매개변수의 위치와 달라도 됨
# - def add(a, b, c):
# - 호출 : add(c=30, a=10, b=20)

# 주의!!
# - 위치 인수와 키워드 인수를 섞어서 사용해도 되지만
# - 호출 시 위치 인수를 키워드 인수보다 앞에 두어야 한다.
# - 호출 : add(10, c=30, b=30) : 위치 인수가 앞에 와야 함
# - 호출 : add(c=30, 10, 20) : 오류 발생
#     - 키워드 인수 뒤에 위치 인수가 올 수 없음


# 키워드 인수 예제
def student_info(name, age, gender):
    student = {
        'name' : name,
        'age' : age,
        'gender' : gender
    }

    return student

print(student_info(name='kim', age=23, gender='여'))
print(student_info('lee', gender='남', age=30))
# print(student_info(gender='남', age=30, 'lee'))
# SyntaxError: positional argument follows keyword argument
