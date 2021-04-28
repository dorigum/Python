# 날짜 출력
# 날짜와 시간을 출력하기 위해서는 datetime 모듈 import 해서 사용
# 모듈 (Module)
# 함수, 변수, 객체들을 모아 놓은 파일
# 모듈 안에 있는 함수 등을 import 문으로 포함해서 사용
# from datetime import date, datetime

from datetime import date, datetime
today = date.today() # 오늘 날짜
year = today.year
month = today.month
day = today.day

print("오늘 날짜 : {0}".format(today))
print("연도 : {0}".format(year))
print("월 {0}".format(month))
print("일 : {0}".format(day))

print("-----------------------------")
now = datetime.now()

year = now.year
month = now.month
day = now.day

hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond

print("현재 날짜 및 시간 : ", now)
print("연도 : ", year)
print("월 : ", month)
print("일 : ", day)

print("시 : ", hour)
print("분 : ", minute)
print("초 : ", second)
print("마이크로초 : ", microsecond)