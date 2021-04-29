# 리스트 반환
def get_names():
    names = []

    for i in range(3):
        name = input("이름 입력 : ")
        names.append(name)

    return names

name_list = get_names()
# print(name_list)


# 리스트에서 각 요소 추출해서 출력 : kim lee park
for name in name_list:
    print(name, end=" ")