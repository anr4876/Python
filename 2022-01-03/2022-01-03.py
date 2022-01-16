# 양자택일
num = 30

if num % 2 == 0 :
    print("짝수")
else :
    print("홀수")
    
# 삼자택일
if num < 5 :
    print("5보다 작습니다.")
    
elif num < 10 :          # elif는 조건이 여러개일때 하나의 출력만 나오도록 한다.
    print("10보다 작습니다.")
    
elif num < 15 :
    print("15보다 작습니다.")

elif num < 20 :
    print("20보다 작습니다.")
    
else :
    print("20보다 크거나 같습니다.")

age = 8

if  age < 14 and age > 7 :
    print("초등학생")
    
if age < 17 and age > 13 :
    print("중학생")
    
if age < 20 and age > 16 :
    print("고등학생")
    
age = 18

if age < 8 :
    print("유치원생")
    
elif age < 14 :
    print("초등학생")

elif age < 17 :
    print("중학생")

elif age < 20 :
    print("고등학생")
    
else :
    print("성인")
    

# 논리연산자 => 두 논리값을 하나의 논리값으로
# 조건1 조건2 => 둘다 맞으면 맞다고 할것인지, 하나만 맞아도 맞다고 하는지.
# 하나만 맞아도 맞다고 하는것 = or 연산
num1 = int(input())
if num1 < 4 or num1 > 5 :
    print ("num1이 4보다 작거나 5보다 크다.")
    
# 둘다 맞아야 맞는 것 = end 연산
if num1 > 4 and num1 <6 :
    print("num1이 4보다 크고 6보다 작다.")
    
# 흐름 제어 => 조건문, 반복문
# while, for
# 반복횟수를 세서 제어한다

num1 = 1

while num1 < 10 :
    print(num1)
    num1 += 1

# for문

for num in range(1, 101, 1) :
    print(num)
    
# 범위가 정해져있는 반복문 : for
# 범위가 정해지지 않아 무한 반복구조 : while

# 자료형, 변수, 조건문, 반복문

# if 문 중첩 => 동시만족

# 반복문 중첩, 이중반복문
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

for num in range(1, 6, 1) :
    print(num, end=" ") # end=" "줄바꿈업이 가로로 출력가능

cnt = 0    
while cnt < 10 :
    for num in range(1, 6, 1) :
        print(num, end=" ")          #가로로출력
    print()                          #줄바꿈
        
    cnt += 1
    
    
for i in range(1, 11, 1) :
    for num in range(1, 6, 1) :
        print(num, end=" ")
    print()
    