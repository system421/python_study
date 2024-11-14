a = [1,4,3]
print("기본리스트:",a)

#원소 삽입
a.append(2)
print("삽입: ",a)

#오름차순 정렬
a.sort()
print("오름차순 정렬:",a)

#내림차숝 정렬
a.sort(reverse=True)
print("내림차순 정렬: ",a)

#원소 뒤집기
a.reverse()
print("원소 뒤집기: ",a)

#특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3추가:",a)

#특정 값의 데이터 갯수 세기
print("값이 2인 데이터 갯수",a.count(2))

#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ",a)