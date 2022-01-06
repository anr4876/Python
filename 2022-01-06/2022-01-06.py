list1 = [1, 2, 3, 4, 5, 6]
for i in range(len(list1)) :
    print(list1[i])
    
# 함수 => 정의, 호출, 매개변수와 인수, 리턴(변환)

def test( ) :
    print("aa")
    print("bb")
    
    
# 리턴(변환)

def aa() :
    c = 10
    return c

print(aa())


# 사람 표현
# 이름, 나이, 사는곳

# 20홍길동, 대전, 홍길동

age1 = 20
home1 = "대전"
name1 = "홍길동"

print("{}사는 {}살 {}입니다.".format(home1, age1, name1))

# 22살, 서울, 홍길순

age2 = 22
home2 = "서울"
name2 = "홍길순"


print("{}사는 {}살 {}입니다.".format(home2, age2, name2))

def introduce(person) :
    print("{}사는 {}살 {}입니다.".format(person[1], person[0], person[2]))

gildong = ["대전", 20, "홍길동"]
introduce(gildong)


# 딕셔너리 => 리스트랑 비슷한데, 리스트는 데이터를 순서(숫자)로 다루고, 딕셔너리는
# 데이터를 또 하나의 데이터와 연결해서 다룬다. => 데이터에 이름은 붙인다.



# apple       ----  사과

# 딕셔너리 사용법

# 코드를 구조화 => 함수
# 한덩어리로 만들기 => 구조화
# 데이터를 구조화 => 딕셔너리
# 리스트는 구조화를 하는데 있어서 좋지는 않다. 데이터 구별, 탑색이 어렵다.
# 딕셔너리를 이용하면 데이터를 쉽고 효율적으로 찾을 수 있다.
# 리스트는 일괄처리 특화

# 선언, 추가, 조회, 수정, 삭제
# 선언
# 비어있는거
list1 = []
dict1 = {}

# 몇개 저장해서 만들기
list2 = [1,2,3,4,5]

# 키(key) - 밸류(value)
dict2 = {"나이" : 20,"고향" :  "대전", "이름" : "홍길동"}

# 조회
print(list2[0])
print(dict2["나이"])

# 추가
list2.append("남자")
print(list2)

ditct2["성별"] = "남자"
print(dict2)


# 수정
list2[0] = 30
print(list2)

dict2["나이"] = 30
print(dict2)


# 삭제 => del()
del(list[3])
print(list2)

del(dict2["성별"])
print(dict2)

