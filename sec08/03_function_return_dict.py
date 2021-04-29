# 딕셔너리 반환
def get_info():
    name = input("이름 입력 : ")
    age = input("나이 입력 : ")
    # 딕셔너리 만들기 (key:value)
    student = {'name': name, 'age': age}

    return student

student_info = get_info()
print(student_info)