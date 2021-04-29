# 파티에 참석한 사람이 다음과 같을 때
# 집합 생성하고 출력
# partyA : "Park", "Kim", "Lee"
# partyB : "Park", "길동", "몽룡"

# 출력
# 파티에 참석한 모든 사람
# 2개의 파티에 모두 참석한 사람
# 파티 A에만 참석한 사람
# 파티 B에만 참석한 사람


partyA = {"Park", "Kim", "Lee"}
partyB = {"Park", "길동", "몽룡"}

# 파티에 참석한 모든 사람
print("파티에 참석한 모든 사람")
print(partyA.union(partyB))
print("----------------------------------------")

# 2개의 파티에 모두 참석한 사람
print("2개의 파티에 모두 참석한 사람")
print(partyA.intersection(partyB))
print("----------------------------------------")

# 파티 A에만 참석한 사람
print("파티 A에만 참석한 사람")
print(partyA.difference(partyB))
print("----------------------------------------")

# 파티 B에만 참석한 사람
print("파티 B에만 참석한 사람")
print(partyB.difference(partyA))