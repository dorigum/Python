# 문자열 관련 메소드 (함수)
# 객체.메소드()
# len()
# count()
# find()
# index()
# split()
# replace()
# join()
# upper() / lower() / capitalize()
# strip() / lstrip() / rstrip()
# isalpha() / isdigit() / isspace()

# len() : 문자열 길이 반환
string = "programming"
print(len(string))

# count() : 문자열 내에 들어 있는 특정 문자(열)의 개수 반환
print(string.count("r"))

# find() : 문자열 내에서 특저 문자열이 존재하는지 여부와 문자열의 시작 위치를 반환
# 존재하지 않으면 -1 반환
# 필요한 문자열만 추출할 수 있도록 필터링하거나 검사할 때 주로 사용

programming = "programming is fun"
print(programming.find("fun"))
print(programming.find("is"))
print(programming.find("data")) # 없으면 -1 반환


# 연습문제
# 우리나라 광역시 중 하나 입력 : 대전
# 정답입니다!

# 우리나라 광역시 중 하나 입력 : 서울
# 틀렸습니다!

cities = "인천 대전 광주 울산 대구 부산"
city = input("우리나라 광역시 중 하나 입력 : ")
if cities.find(city) != -1:
    print("정답입니다!")
else:
    print("틀렸습니다!")


# 이메일 주소를 입력받아서, 이메일 형식이 아니면
# "이메일 형식이 아닙니다." 출력
# 이메일 입력 : ab.com
# 이메일 형식이 아닙니다.

# 이메일 형식이 아닌 경우
# - @ 없는 경우
# - . 없는 경우 ...

email = input("이메일 입력 : ")
if(email.find("@") == -1 or                     # @이 없는 경우
    email.find(".") == -1 or                    # .이 없는 경우
    email.find("@") > email.find(".") or        # @과 .이 위치가 바뀐 경우
    email.find(".") - email.find("@") < 2 or    # @과 . 사이에 문자가 없는 경우
    email.find("@") == 0 or                     # @ 앞에 없는 경우
    len(email) - email.find(".") <= 1 or        # . 뒤에 문자가 없는 경우
    email.count("@") >= 2 or                    # @이 두 번 이상 있는 경우
    email.count(".") >= 2):                     # .이 두 번 이상 있는 경우
    print("이메일 형식이 아닙니다.")

print("이메일 형식입니다.")


# split() : 구분자를 기준으로 문자열을 분리
# 리스트 반환
# 구분자 : 기본은 공백
# 구분자 지정 : "-", ":", ",", ...

# replace() : 전체 문자열에서 특정 문자열을 찾아 다른 문자열로 변환
# 전체문자열.replace(찾는 문자열, 변경할 문자열)

# isalpha() : 문자 여부 결과 반환 (True, False)
# isdigit() : 숫자 여부 결과 반환 (True, False)
# isspace() : 하나의 문자에 대해 공백 여부 결과 반환 (True, False)
# isalnum() : 문자 또는 숫자 여부 결과 반환

phone = input("전화번호 입력 (숫자만) :")

if phone.isdigit():
    pass
else:
    print("숫자만 입력하세요.")


# 문자열을 입력하고 알파벳, 숫자, 스페이스, 기타 개수 출력
# 문장을 입력하세요 : 나의 email 주소는 python777@naver.com 입니다!
# 알파벳 : 개
# 숫자 : 개
# 스페이스 : 개
# 기타 : 개

alphas = digits = spaces = others = 0
string = input("문장을 입력하세요 : ")

for c in string:
    if c.isalpha():
        alphas += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        spaces += 1
else:
    others += 1

print("알파벳 : %d개" % alphas)
print("숫자 : %d개" % digits)
print("스페이스 : %d개" % spaces)
print("기타 : %d개" % others)