# 입력 - 출력 (프로그램)

# print() 출력
print("출력")
# input() 입력
a = input()
print(a)

a = input()
b = input()
print(a + b) # input()은 문자취급

print(a + b) # print안에서는 형변환을 사용 못한다.

 
num1 = input("첫번째 숫자를 입력해주세요 : ")
num2 = input("두번째 숫자를 입력해주세요 : ")
# input("")안에 원하는 문자를 넣을수있다.
print(num1 + num2) 


# 자료형 -> 문자형, 정수형, 실수형

# 산술연산자
# % : 나머지 구하기
# / : 결과가 소수
# // : 결과가 정수
# += : 자기 자신한테 더한다.(복합대입연산자)

print(10 % 3)
print(10 / 3)
print(10 // 3)

# 복합대입연산자 활용 
# i = i + 1 => i += 1
# num = num + i => num += i

# 문자(str), 정수(int), 실수(float), 논리(bool)
# 비교연산자
10 > 5 # True
4 >= 4 # True
4 == 4 # True
4 != 4 # Fa lse

bool1 = True
bool2 = 4 < 10

print(bool1)
print(bool2)

# 흐름 제어 -> 조건문, 반복문

num1 = 1

if num1 < 10 :
    print('num1num1')    # 들여쓰기, 인덴트


# 날씨에 따른 인사

# "비", "눈", "맑음"
weather = 1 #1. 비 , 2. 눈 , 3. 맑음 

if weather == 1 :
    print("비가 오니까 우산 챙기세요")

if weather == 3 :
    print("날이 맑으니까 나들이 나가세요")

if weather == 2 :
    print("눈이 오니까 넘어지지 않게 조심하세요")

num = 8

if num < 5 :
    print("5보다 작습니다.")

if num < 10 :
    print("10보다 작습니다.0")

if num < 15 :
    print("15보다 작습니다.")


#양자택일
#if num :
#eslo 

