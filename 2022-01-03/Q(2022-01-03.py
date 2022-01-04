# 문제 : 할인 대상인지 아닌지 출력해주세요.
# 조건 : 나이가 19세 이하이거나 60세 이상이면 할인 대상입니다.
# 나이를 입력받고 해당 나이가 할인 대상인지 아닌지 출력해주세요.

### 입출력 예시
# 나이를 입력해주세요 : 22
# 할인대상이 아닙니다.

# 나이를 입력해주세요 : 10
# 할인대상입니다.

# 나이를 입력해주세요 : 70
# 할인대상입니다.

num1 = int(input("나이를 입력해주세요 : "))
if num1 <= 19 or num1 >= 60 :
    print("할인대상입니다.")
    
else :
    print("할인대상이 아닙니다.")
    
#===============================================
'''
어떤 차의 높이가 170cm 입니다..

이 차는 3개의 터널을 차례대로 지나게 될 것입니다.

터널의 높이가 차의 높이보다 같거나 낮다면 차는 터널과 충돌하여 사고가 납니다.

터널의 높이를 순서대로 3개 입력한 후 터널을 무사히 잘 통과하면 PASS 를 출력하고, 사고가 난다면 CRASH 를 출력하세요.

예시 ) tunel1 = 162
       tunel2 = 180
       tunel3 = 166

터널의 높이가 위와 같다면 tunel1과 tunel3에서 걸리므로 CRASH
'''

car = 170

t1 = 168
t2 = 178
t3 = 188
# CRASH


# t1 = 178
# t2 = 178
# t3 = 188
# PASS

tunel1 = input("1터널 높이를 입력하시오 : ")
tunel2 = input("2터널 높이를 입력하시오 : ")
tunel3 = input("3터널 높이를 입력하시오 : ")
tunel1 = int(tunel1)
tunel2 = int(tunel2)
tunel3 = int(tunel3)

if tunel1 <= 170 :
    print("CRASH")
elif tunel2 <= 170 :
    print("CRASH")
elif tunel3 <= 170 :
    print("CRASH")
else :
    print("PASS")
    
car = input("차의 높이를 입력하세요 : ")
tunel1 = input("1터널의 높이를 입력하세요 : ")
tunel2 = input("2터널의 높이를 입력하세요 : ")
tunel3 = input("3터널의 높이를 입력하세요 : ")

car = int(car)
tunel1 = int(tunel1)
tunel2 = int(tunel2)
tunel3 = int(tunel3)

if car <= tunel1 :
    print("CRASH")
    
elif car <= tunel2 :
    print("CRASH")
    
elif car <= tunel3 :
    print("CRASH")
    
else :
    print("PASS")

# 반복문을 이용해 안녕하세요를 10번 출력해주세요.

num1 = 1
while num1 <= 10 :
    print("안녕하세요.")
    num1 += 1

# 반복문을 이용해 1 ~ 10까지 출력해주세요.

num1 = 1
while num1 <= 10 :
    print(num1)
    num1 += 1
    
# 문제 : 99단 8단을 출력해주세요.
# 조건 : while문을 사용해주세요.

"""
출력 양식 
== 8단 ==
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
"""



# 수정가능 시작

num1 = 1
num2 = input("숫자를 입력하시오 : ")
num1 = int(num1)
num2 = int(num2)
while num1 < 10 :
    print("{} * {} = {}".format(num2, num1 , num1 * num2))
    num1 += 1
    
# for문으로 8단 만들기
num1 = int(8)

for num2 in range(1, 10, 1) :
    print("{} X {} = {}".format(num1, num2, num1 * num2))
    
    
#구단 2~9단 출력해주세요.
for num1 in range(2, 10, 1) :
    for num2 in range(1, 10, 1) :
        print("{} * {} = {}".format(num1, num2, num1 * num2), end=" ")
    print()    