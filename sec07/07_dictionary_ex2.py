# 딕셔너리를 이용해 사용자로부터 영단어와 뜻을 입력 받아서 사전을 구성하고
# 사용자가 입력한 단어를 검색해서 뜻을 출력하는 프로그램


ek_dic = dict()

# 단어 등록
while True:
    eng = input("\n영어 단어 등록 (종료는 quit) : ")

    if eng == "quit":
        break
    elif eng not in ek_dic:
        kor = input("%s의 뜻 입력 (종료는 quit) : " % eng)
        ek_dic[eng] = kor
    else:
        print("%s는 이미 등록된 단어입니다." % eng)

print()


# 단어 검색
while True:
    eng = input("\n검색할 단어 입력 (종료는 quit) : ")

    if eng == "quit":
        break
    elif eng in ek_dic:
        print("%s의 뜻은 %s입니다." % (eng, ek_dic[eng]))
    else:
        print("%s는 사전에 없는 단어입니다." % eng)

print("\n종료합니다.")
