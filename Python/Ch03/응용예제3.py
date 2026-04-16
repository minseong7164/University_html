print("학생 성적을 입력하세요. (이름, 국어, 영어, 수학)")
print("입력예시: 홍길동 80 90 85")
print("최대 3명까지 입력할 수 있습니다.\n")

data1 = input("첫 번째 학생 정보 입력: ")
name1, kor1, eng1, math1 = data1.split()
kor1, eng1, math1 = int(kor1), int(eng1), int(math1)
avg1 = (kor1 + eng1 + math1) / 3

data2 = input("두 번째 학생 정보 입력: ")
name2, kor2, eng2, math2 = data2.split()
kor2, eng2, math2 = int(kor2), int(eng2), int(math2)
avg2 = (kor2 + eng2 + math2) / 3

data3 = input("세 번째 학생 정보 입력: ")
name3, kor3, eng3, math3 = data3.split()
kor3, eng3, math3 = int(kor3), int(eng3), int(math3)
avg3 = (kor3 + eng3 + math3) / 3

print("\n[학생 성적표]")
print("=" * 50)
print("%-10s %-5s %-5s %-5s %-7s" % ("이름", "국어", "영어", "수학", "평균"))
print("=" * 50)

print("%-10s %5d %5d %5d %7.2f" % (name1, kor1, eng1, math1, avg1))
print("%-10s %5d %5d %5d %7.2f" % (name2, kor2, eng2, math2, avg2))
print("%-10s %5d %5d %5d %7.2f" % (name3, kor3, eng3, math3, avg3))

print("=" * 50)
print("총 학생 수: 3")
