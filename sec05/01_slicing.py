# 문자열 인덱싱 (indexing)
# 인덱스로 문자의 위치를 나타내는 것
# 인덱스(첨자) : 문자의 위치, 0부터 시작
# string[0] : 인덱스 0번째 문자 (첫번째 문자)
# string[-1] : 마지막 문자

# 슬라이싱 (slicing)
# 문자열 중에서 일부분을 추출하는 것 (잘라내는 것)
# 인덱스 사용
# string[0:n] : 0부터 n-1번째까지의 문자열 추출
# string[n:] : n부터 끝까지
# string[:n] : 0부터 n-1까지
# string[-1:] : 마지막 문자 (마지막에서 끝까지)
# string[:-1] : 처음부터 마지막 -1
# string[:] : 잔체 문자열 반환

python = "python programming is fun"
java = "java is also fun"

print(python[5:15])
print(python[:])
print(python[5:])
print(python[:15])
print(python[:-1])
print(java[:])

print(java[0:10:2])  # 0~9까지 2씩 추가

# in / not in
# 문자열 안에 특정 문자열이 포함되어 있는지 여부 확인
# 결과는 True, False

string = "python programming"

print("python" in string)

if "java" in string:
    print("있음")
else:
    print("없음")

ids = ["sun", "flower", "moon", "sky"]
id = input("id 입력 : ")

if id in ids:
    print("로그인 성공!")
else:
    print("로그인 실패!")