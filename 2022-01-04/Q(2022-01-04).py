# 1. 1 ~ 100 까지 짝수만 출력

for num in range(1, 101, 1) :
    if num % 2 == 0 :
        print(num, end=" ")

# 2. 100 ~ 200 사이의 홀수만 출력
for i in range(101, 201, 1) :
    if i % 2 == 1 :
        print(i, end=" ")
            
# 1 ~ 500 사이의 수 중 4의 배수만 출력

for i in range(1, 501, 1) :
    if i % 4 == 0 :
        print(i, end=" ")

# n과 m 사이의 수 중 k의 배수 출력
n = 10
m = 30
k = 3

for i in range(n, m+1, 1) :
    if i % k == 0 :
        print(i)
        
        
# 1부터 10까지 합을 구해주세요.
num = int(0)
for i in range(1, 11, 1) :
    num += i
            
    
print(num)

#==================================================================

# n부터 m까지의 수중 3의 배수이거나 7의 배수인 수들의 합 구하기

# 이 값들을 바꿔가면서 실행해주세요
n = 4
m = 100
num = 0
for i in range(n, m+1, 1) :
    num1 = i % 3
    num2 = i % 7
    if num1 == 0 or num2 == 0 :
        print(i, end=" ")
        num += i

#=========================================================================

'''
축구 경기가 진행중이다. 축구경기 타임은 총 90분이고,

현재 A팀이 0점, B팀이 2점인 상황에서, A팀은 최고의 스트라이커인 손흥민을 투입하기로 결정했다.

손흥민은 투입과 동시에 그리고 5분마다 골을 넣을 수 있는 능력을 가지고 있다.

만약 80분에 투입이 되면 80분에 곧바로 골을 넣게되고 85분에 골을 넣음으로서 동점이 가능하게 된다.

(90분이되면 경기가 바로 종료되므로 골을 넣을 수 없다. 해당 경기의 심판은 추가시간을 주지 않는 것으로 유명하다.)

현재 경기타임 time과 A팀의 득점 score가 주어질 때, 손흥민을 투입하면 A팀의 최종 득점은 몇 점인지 출력하시오.
'''
time = 74;
score = 0;

if time % 5 != 0 :
    score += 1
for i in range(time, 90, 1) :
    if i % 5 == 0 :
        score += 1
          
    
print(score)  

#=========================================================================
    
# 구구단을 2~9단까지 출력

for i in range(2, 10, 1) :
    for j in range(1, 10, 1) :
        print("{} X {} = {}".format(i, j, i*j))

# 구구단을 2~9단까지 작수곱만 출력.
'''
2 * 2 = 4
    4
    6
    8
3 * 2 = 6
    4
    6
    8
'''
for i in range(2, 10, 1) :
    for j in range(1, 10, 1) :
        if j % 2 == 0 :
            print("{} X {} = {}".format(i, j, i*j))
# 2. 홀수단만 나오게    

''' 
3단
5단
7단
9단
'''
for i in range(2, 10, 1) :
    if j % 2 != 0 :
        for j in range(1, 10, 1) :
            print("{} X {} = {}".format(i, j, i*j))
            
            
# 구구단을 가로로 나오게 해주세요. 

'''
2 * 1 = 2   3 * 1 = 3   4 * 1 = 4          9 * 1 = 9
2 * 2 = 4   3 * 2 = 6   4 * 2 = 8          9 * 2 = 18
2 * 3 = 6   3 * 3 = 9   4 * 3 = 12         9 * 3 = 27 
2 * 4 = 8   3 * 4 = 12  4 * 4 = 16         9 * 4 = 36
2 * 5 = 10  3 * 5 = 15  4 * 5 = 20   ...   9 * 5 = 45
2 * 6 = 12  3 * 6 = 18  4 * 6 = 24         9 * 6 = 54
2 * 7 = 14  3 * 7 = 21  4 * 7 = 28         9 * 7 = 63
2 * 8 = 16  3 * 8 = 24  4 * 8 = 32         9 * 8 = 72
2 * 9 = 18  3 * 9 = 27  4 * 9 = 36         9 * 9 = 81

'''
for i in range(1, 10, 1) :
    
    for j in range(2, 10, 1) :
        print("{} X {} = {}".format(j, i, i*j), end="   ")
    print("\n")
        
        
#===========================================================================        

# 구구단은 n단 ~ m단 중 홀수단만 1 ~ limit 까지 곱 중 짝수곱만 출력해주세요.

n = 4;
m = 19;
limit = 11;

'''  출력 예시

5 * 2 = 10
5 * 4 = 20
5 * 6 = 30
5 * 8 = 40
5 * 10 = 50

7 * 2 = 14
7 * 4 = 28
7 * 6 = 42
7 * 8 = 56
7 * 10 = 70
...
...
19 * 2 = 38
19 * 4 = 76

'''

for i in range(n, m + 1) :
    for j in range(1, 11) :
        if i % 2 != 0 :
            print("{} X {} = {}".format(i, j, i*j), end="   ")
            
            
for i in range(1, limit + 1) :
    for j in range(1, 11) :
        if i % 2 == 0 :
            print("{} X {} = {}".format(i, j, i*j), end="   ")
            
            
            
            
#=====================================================================
y = 3

#  print("*", end="")


# 출력
'''

***
***
***

'''
for i in range(1 , y + 1) :
    for j in range(1, y + 1) :
        print("*",end="     " )
    print("\n")
y = 5

# 출력
'''


*****
*****
*****
*****
*****

'''
for i in range(1 , y + 1) :
    for j in range(1, y + 1) :
        print("*",end="     " )
    print("\n")

y = 7
# 출력
'''

*******
*******
*******
*******
*******
*******
*******

'''
for i in range(1 , y + 1) :
    for j in range(1, y + 1) :
        print("*",end="     " )
    print("\n")
    
#===============================================================

y = 3

    
# 출력
'''

  *
 **
***

'''
for i in range(1 , y + 1) :
    num = y - i
    for j in range(1 , num + 2) :
        
        
        print(" ", end="    ")
    for k in range(1 , i + 1) :
        print("*", end="    ")
        
    print("\n")
y = 5
# 출력
'''

    *
   **
  ***
 ****
*****

'''
for i in range(1 , y + 1) :
    num = y - i
    for j in range(1 , num + 2) :
        
        
        print(" ", end="    ")
    for k in range(1 , i + 1) :
        print("*", end="    ")
        
    print("\n")
y = 7
# 출력
'''

      *
     **
    ***
   ****
  *****
 ******
*******

'''
for i in range(1 , y + 1) :
    num = y - i
    for j in range(1 , num + 2) :
        
        
        print(" ", end="    ")
    for k in range(1 , i + 1) :
        print("*", end="    ")
        
    print("\n")
    
    
#===============================================================
y = 3

# print("*", end="")

for i in range(1 , y + 1) :
    num = y - i
    for j in range(num) :
        
        
        print(" ", end="    ")
    for k in range(i) :
        print("*", end="    ")
        
    print("\n")
    
# 출력
'''

*
**
***

'''

y = 5

# 출력

for i in range(1 , y + 1) :
    num = y - i
    for j in range(num) :
        
        
        print(" ", end="    ")
    for k in range(i) :
        print("*", end="    ")
        
    print("\n")
    
'''

*
**
***
****
*****

'''

y = 7
for i in range(1 , y + 1) :
    num = y - i
    for j in range(num) :
        
        
        print(" ", end="    ")
    for k in range(i) :
        print("*", end="    ")
        
    print("\n")
    
# 출력
'''

*
**
***
****
*****
******
*******

'''

#==위에 문제 풀다가 나온 변형
y = 3

for i in range(1 , y + 1) :
    for j in range(1 , i + 1) :
        print(" ", end="    ")
    for k in range(1 , y - i + 2) :
        print("*", end="    ")
        
    print("\n")
    
y = 5

for i in range(1 , y + 1) :
    for j in range(1 , i + 1) :
        print(" ", end="    ")
    for k in range(1 , y - i + 2) :
        print("*", end="    ")
        
    print("\n")
    
y = 7

for i in range(1 , y + 1) :
    for j in range(1 , i + 1) :
        print(" ", end="    ")
    for k in range(1 , y - i + 2) :
        print("*", end="    ")
        
    print("\n")
    

    
#==============================================================


list1 = [2,5,9,11,23,51,26,38,41,93,101]

# 위 리스트의 모든 값을 출력해주세요.
print(list1)
# 출력 : 2, 5, 9, 11, 23, 51, 26, 38, 41, 93, 101

# 위 리스트의 '홀수번째 인덱스' 값만 출력해주세요.
for i in range(10) :
    if i % 2 != 0 :
        print(list1[i], end=" ")
# 출력 : 5, 11, 51, 38, 93

# 위 리스트의 '짝수값'만 출력해주세요. 
for i in range(10) :
    if list1[i] % 2 == 0 :
        print(list1[i], end=" ")
# 출력 : 2, 26, 38
print("\n")
# 위 리스트의 값으로 구구단을 만들어주세요
for i in range(10) :
    for j in range(1, 10) :
        print("{} X {} = {}".format(list1[i], j, list1[i]*j))
# 출력 : 2단, 5단, 9단, 11단, 23단, 51단, 26단, 38단, 41단, 93단, 101단

# 위 리스트의 값을 거꾸로 출력해주세요.
for i in range(10) :
    num = 10- i
    print(list1[num], end='')
# 출력 : 101, 93, 41, 38, 26, 51, 23, 11, 9, 5, 2

