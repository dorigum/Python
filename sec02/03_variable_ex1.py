# 변수 선언 후 값 저장하고 출력
# 성명 : 홍길동
# 학번 : 2021001
# 학년 : 4
# 학점 : A
# 평균 : 93.5

name = "홍길동"
stdnum = "2021001"
year = 4
grade = 'A'
average = 93.5

print("성명 : ", name)
print("학번 : ", stdnum)
print("학년 : ", year)
print("학점 : ", grade)
print("평균 : ", average)

# 포맷 코드 사용 출력 : print("서식" % 값)
print("성명 : %s" % name)
print("학번 : %s" % stdnum)
print("학년 : %d" % year)
print("학점 : %c" % grade)
print("평균 : %.2f" % average)

# 퍼센트로 % 출력
print("10%")
rate = 80
print("출석률 : %d%%" % rate)

# 2개 이상의 값 출력 : 반드시 괄호로 묶는다 (괄호 () 없으면 오류)
total = 250
avg = 83.33
print("%d, %.2f" % (total, avg))