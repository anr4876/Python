# 함수를 완성하여 아래처럼 실행되도록 해주세요.
# 숫자출력기(2) # 2출력.
# 숫자출력기(5) # 5출력.
# 숫자출력기(10) # 10출력.

def number(num1) :
    print(num1)
    
number(2)
number(5)
number(10)

#=====================================================================
# 함수를 완성시켜 아래와 같이 작동하도록 해주세요.

#v1
#자기소개()
# 출력 :  안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 


def myname(name) :
    for i in range(1, 10) :
        print("안녕하세요. 저는 {}입니다.".format(name))
        
        
myname("dustjdanr")

#========================================================================

# 매개변수로 받은 숫자만큼 여러번 인사하는 함수를 만들어주세요. 

def myname(num, name) :
    for i in range(num) :
        print("안녕하세요. 저는 {}입니다.".format(name))
        


        

# v2
# 자기소개(10)
# 출력 :  안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
myname(10, "dustjdanr")

print("\n\n")
# 자기소개(5)
# 출력 : 안녕하세요. 저는 누구누구입니다
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 
#        안녕하세요. 저는 누구누구입니다 

myname(5, "dustjdanr")
print("\n\n")
# 자기소개(1)
# 출력 : 안녕하세요. 저는 누구누구입니다

myname(1, "dustjdanr")


#=========================================================
# 다국어인사에 매개변수로 1을 넘기면 안녕하세요. 2를 넘기면 하이!, 3을 넘기면 봉쥬르
# 다국어인사에 매개변수로 인사의 횟수와 언어를 넘겨서 해당 횟수만큼 해당 언어로 인사하게 해주세요.

helo = [0,"안녕하세요","하이!","봉쥬르"]
def 다국어인사2(lang) :
    print(helo[lang])

다국어인사2(3) # 봉쥬르 출력
다국어인사2(1) # 안녕하세요 출력
다국어인사2(2) # 하이 출력

# 다른 방법 (if)
# def 다국어인사2(lang) :
#     if lang == 1 :
#         print("안녕하세요.")
#     elif lang == 2 :
#         print("봉쥬르")  
#     elif lang == 3 :
#         print("하이")

def 다국어인사(lang, count) :
    for i in range(count) :
        print(helo[lang])


다국어인사(3, 3) # 봉쥬르 3번 출력
다국어인사(1, 5) # 안녕하세요 5번 출력
다국어인사(2, 1) # 하이 1번 출력


# 10을 리턴해주는 함수 완성

def func1(num) :
    return num

a = func1(10)
    
print(a) 

#출력 : 10

b = func1(10)
print(b)

#출력 : 10


# 매개변수 값을 그대로 리턴해주는 함수 완성
def func2(num) :
    return num

c = func2(22)
print(c)
# 출력 : 22
  
d = func2(55)
print(d)
# 출력 : 55


# 매개변수 값을 제곱해서 리턴해주는 함수 완성

def func3(num) :
    return num * num

e = func3(10)
print(e)

# 출력 : 100

f = func3(5)
print(f)
# 출력 : 25



# 매개변수를 더해서 리턴해주는 함수 완성
def func4(num1, num2) :
    num = num1 + num2 
    return num
g = func4(10, 30)
print(g)
# 출력 : 40

h = func4(20, 50)
print(h)
# 출력 : 70

#==============================================================

# num이 홀수인지 짝수인지 판별해주는 함수 완성
def is_even(num) :
    if num % 2 == 0 :
        print("짝수입니다.")
    elif num % 2 != 0 :
        print("홀수입니다.")


def print_even(num) :

  if is_even(num) == True:
    print("짝수입니다.")
  else :
    print("홀수입니다.")



print_even(2) # 짝수입니다.
print_even(3) # 홀수입니다.

#================================================================

# 문제 : 1 ~ n까지의 수중 3의 배수의 합을 구해주세요.



# 어떤수가 3의 배수인지 아닌지 체크하는 함수
def is_three_multiple(num) :
    if num % 3 != 0 :
        print("3의 배수가 아닙니다")
    else :
        print("3의 배수입니다.")
        


# 1 ~ n까지의 수중 3의 배수의 합을 구하는 함수

def get_sum_of_three_multiple(n) :
    num = 0
    for i in range(n) :
        if i % 3 == 0 :
            num += i
    return num
       

            
    
        
    
result = get_sum_of_three_multiple(100)
print("결과 : {}".format(result))
    

# 출력 => 1683

