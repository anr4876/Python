# 리스트

list1 = [2, 5, 9, 11, 23, 51, 26, 38, 41, 93, 101]

# Len - 리스트의 길이를 구해줌
print("list1의 길이 : {}".format( len(list1) ))

for i in range(len(list1)) :
    print(list1[i], end=" ")
    
print('\n')    

# 인덱스의 홀수번만 출력
for i in range(len(list1)) :
    if i % 2 != 0 :
        print(list1[i], end=" ")
        
print('\n')    
    
# 홀수만 출력
for i in range(len(list1)) :
    if list1[i] % 2 != 0 :
        print(list1[i], end=" ")
        
print('\n')    
        
# 짝수만 출력
for i in range(len(list1)) :
    if list1[i] % 2 == 0 :
        print(list1[i], end=" ")
        
        
# 위 리스트의 값으로 구구단 만들기

for i in range(len(list1)) :
    dan = list1[i]
    
    for gop in range(1, 10) :
        print("{} X {} = {}".format(dan, gop, dan * gop))
        
# 리스트 거꾸로 출력하기
       
for i in range(10, -1, -1) :
    print(list1[i], end="  ")
                       
# range(a, b) 를 리스트로 바꾸기

list1 = list(range(1, 101))
print(list1, end=",")

# for 문에서 range() 위치는 리스트 위치이다. 따라서 range()대신 리스트를 넣어도 괜찮다.
        
for i in list1 :
    print(i,end="  ")
                       
print("\n")              
# 리스트의 짝수번째 값 1증가시키기
list2 = [1,2,3,4,5,6]


for i in range(len(list2)) :
    if i % 2 == 0 :
        list2[i] += 1
        
print(list2)


# 리스트에서 짝수만 출력

list1 = [11,22,33,44,55,66,77,88,99,110]

list2 = [1,2,3,4,5,6,7,8,9,10]

for num in list1 :
    if num % 2 == 0 :
        print(num)


for num in list2 :
    if num % 2 == 0 :
        print(num)
        
# 변수 => 값을 저장하고 재사용       
# 함수 => 절차를 저장하고 재사용하고 싶을 때

# 함수 선언
def test(list4) : 
    for num in list4 :
        if num % 2 == 0 :
            print(num, end=" ")
            
test(list1) # 사용하겠다는 코드 작성 => 호출 함수

#  함수는 선언 => 만들어야 사용 가능
# 함수는 호출해야 한다. => 사용해야만 작동한다.
# 함수에 인수를 넘길 수 있고, 함수는 매개변수를 이용해 받을 수 있다. => 값을 넘기고 받을 수 있다.

# 함수 사용하면 좋은 점 : 
# 1. 코드를 재사용.
# 2. 코드를 구조화 한다. => 코드를 한덩어리로 본다.

# 

print("\n")
def plus(X) :
    return X + 10
plus(5)

def double(X) :
    return X * 2
    
print(double(plus(5)))