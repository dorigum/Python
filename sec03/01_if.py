# 제어문
# 조건문 : if 문
#         if ~ else ~
#         if ~ elif ~ else
# 반복문 : for 문
#         while 문
# 기타 : break 문
#       continue 문

# if 문 형식 : 콜론, 들여쓰기(탭 또는 스페이스 4칸)
# if(조건식) :
#     참일 경우 수행되는 문장
#
# if(조건식) :
#     참일 경우 수행되는 문장
# else :
#     거짓일 경우 수행되는 문장

password = 1234

if password == 1234:
    print("비밀번호가 일치합니다.")
else:
    print("비밀번호가 일치하지 않습니다.")


# 아무것도 수행하지 않을 경우 : pass

password = 12345
if password == 1234:
    print("비밀번호가 일치합니다.")
else:
    pass
