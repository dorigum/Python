# 딕셔너리 선언
dictionary = {
    "name" : "버섯 불고기 덮밥",
    "type" : "덮밥",
    "ingredient" : ["소고기", "버섯", "양파", "간장", "설탕"],
    "origin" : "한국"
}

# 딕셔너리 내용 출력
print("요리명 : ", dictionary["name"])
print("종류 : ", dictionary["type"])
print("재료 : ", dictionary["ingredient"])
print("원산지 : ", dictionary["origin"])

# 딕셔너리 값 변경
# 버섯 불고기 덮밥 -> 한우 버섯 불고기 덮밥
dictionary["name"] = "한우 버섯 불고기 덮밥"
print("요리명 : ", dictionary["name"])

# 재료가 리스트로 출력 -> 각 요소 출력으로 변경
# ['소고기', '버섯', '양파', '간장', '설탕'] -> 소고기 버섯 양파 간장 설탕

# 재료 추출
ingredient = ""
for i in dictionary["ingredient"]:
    ingredient += i + " "

print(ingredient)

print("요리명 : ", dictionary["name"])
print("종류 : ", dictionary["type"])
print("재료 : ", ingredient)
print("원산지 : ", dictionary["origin"])