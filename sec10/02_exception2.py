# 예외 처리

# 에러 종류와 상관없이
# 에러가 발생하기만 하면 except 블록 수행
try:
    # print(10/0)
    print("나이" + 23 + "살")
except:
    print("오류 발생")


# 모든 에러를 처리할 수 있도록 최상위 Exception 적어도 됨

try:
    print(10/0)
except Exception:  # 범위가 광범위하다는 경고
    print("오류 발생")


# 구체적으로 에러 종류 명시

try:
    print(10/0)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")


try:
    num = int(input("숫자 입력 : "))
except ValueError:
    print("숫자가 아닙니다.")
    

# 에러 종류 명시 as 에러 메시지 변수
# 에러 메시지 변수를 사용해서 에러 내용 출력
try:
    print(10/0)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.", e)


a = [1, 2, 3]

try:
    print(10/0)
    print(a[4])
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.", e)
except IndexError as e:
    print("인덱스 범위를 벗어났습니다.", e)
    
# 첫번째 에러만 처리됨

try:
    print(10/0)
    print(a[4])
except (ZeroDivisionError, IndexError):
    print("오류가 발생했습니다.")


try:
    print(10/0)
    print(a[4])
except:
    print("오류 발생")


# 오류가 발생할 때 메시지 출력하지 않고 그냥 넘어가는 방법
# finally : 예외 발생 여부에 상관없이 항상 수행되는 블록
try:
    f = open("exception.txt", 'r')
except FileNotFoundError:
    pass
else:
    data = f.read()
    f.close()
finally:
    print("종료")