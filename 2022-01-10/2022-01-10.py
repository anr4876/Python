
# # 구조가 점점 확작
# # 변수 -> 리스트,딕셔너리
# # 일반적 코드 작성 -> 코드 덩어리(함수)

# # 사람

# def introduce(p) :
#     print("{}살 {} 입니다.".format(p[age], p[name]))



# p1 = {"age" : 20, "name" : "홍길동"}
# p2 = {"age" : 21, "name" : "홍길순"}
# p3 = {"age" : 22, "name" : "홍길영"}

# # class

# class person :
#     age = 20
#     name = "홍길동"
    

# class person :
#     age = 21
#     name = "홍길순"
    

# class person :
#     age = 22
#     name = "홍길영"
    
# # 객체(인스턴스) 만들기

# p1 = person()
# p2 = person()    

class person :
    
    def __init__(self, age, name) :
        self.age = age
        self.name = name
    
    def introduce(self) :
        print("{}살 {}입니다.".format(self.age, self.name))  
                  
p1 = person(20, "홍길동")                
p2 = person(21, "홍길순")                
p3 = person(22, "홍길영")
 
        
p1.introduce()    
p2.introduce()        
          
# class => 비슷한 구조끼리 묶는다.
# 프로그램 데이터가 본질 => 데이터 처리(함수)
# 함수는 데이터에 의존적이다 
# 안전한 프로그래밍, 유연한 프로그래밍          
# 데이터 => 정보/속성, 함수 => 기능/동작 ==> 모든 사물은 상태/동작
# 객체 == 사물
# 객체지향 프로그래밍

# 이미 존재하는 것을 조립
# 패키지로 제품이 나옴 객체 묶음

# 변수 > 리스트,딕셔너리
# 코드 > 함수

# 변수 + 함수 > 객체

# 객체를 비롯한 다양한 자원을 파일에 모아두는 것. --> 모듈

# 파이썬 => 패키지 관리자 (pip )



