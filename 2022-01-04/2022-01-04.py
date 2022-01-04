cnt = 0

while cnt < 10 :
    print('aa', end='')
    print('bb')     
    cnt += 1
    
for i in range(1, 10, 1) :
    print("")


for i in range(1, 6, 1) :
    for j in range(1, 6, 1) :
        print (j, end=" ")
        
        
# 자료형
# 문자, 정수, 실수, 논리 => 단일자료형
# 컬렉션 자료형  => 리스트


kim = 90
lee = 77
choi = 100
park = 66
cho = 80


# 모든 변수의 값을 알고싶다. => 모든 변수명을 알아야한다.
# 데이터 => 변수에 저장 => 변수명
# 변수를 사용하려면 변수명 알아야함
# 학번 부여
# 데이터의 순서를 부여 


scores = [90, 77, 100, 66, 80]   # 변수에 순서를 주고 저장
print(scores[0])                 # 순서는 0부터
# print(scores[n - 1])   n번째 자료

print(kim)
print(cho)
print(park)
print(choi)
print(lee)

print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print(scores[4])

for i in range(5) :
    print(scores[i])
    
# 리스트 간단 사용법

list1 = [1, 2, 3, 4, 5, 6]   # 리스트

# 리스트 값을 사용하는 법 => 순번(인덱스)으로 접근
print(list1[3] + 2)

print(list1)

# 리스트안에 값을 변환하는 법 => 인덱스로 선택해서 대입
list1[0] = 100
print(list1)

# 값을 삭제 => del () => 지우고싶은 인덱스를 선택해서 del() 안에 삽입
del(list1[3])
print(list1) 

# 값을 추가 => append() => 추가하고싶은 값을 넣으면 됨

list1.append(10)

print(list1)

# 컬렉션 자료형 => 리스트, 튜플, 딕셔너리, 셋
# 추가, 조회, 수정, 삭제 사용가능
