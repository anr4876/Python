# # 구구단 7단을 출력해주는 함수를 만들어주세요.

def gugu7() :
    for gop in range(9) :
        print("{} X {} = {}".format(7 , gop, 7 * gop))
            

gugu7() # 출력 : 7단7




# # 원하는 이름을 출력해주는 함수를 만들어주세요(매개변수)

def print_name(name) :
    print("저의 이름은 name 입니다.")

print_name("홍길동") # 출력 : 홍길동




# # 구구단 원하는 단을 출력해주는 함수를 만들어주세요.(매개변수)

def my_gugu(num) :
    for gop in range(9) :
        print("{} X {} = {}".format(num , gop, num * gop))

my_gugu(8)
# 출력 : 8단

my_gugu(5)
# 출력 : 5단



# # 구구단을 1단부터 원하는 단까지 출력해주는 함수를 만들어주세요.(매개변수)

def one_to_n_gugu(num) :
    for dan in range(num) :
        for gop in range(9) :
            print("{} X {} = {}".format(num , gop, num * gop))

one_to_n_gugu(11) # 출력 1 ~ 11단까지 출력
one_to_n_gugu(20) # 출력 1 ~ 20단까지 출력

# True를 리턴하는 함수를 만들어주세요. 그리고 my_bool 변수에 저장해주세요. 그리고 my_bool을 출력해주세요.(리턴)

def get_true() :
    return True

myBool = get_true()
print(myBool) # 출력 : True



# 자신의 이름을 리턴하는 함수를 만들고 변수 my_name에 저장해주세요. 그리고 my_name을 출력해주세요.(리턴)

def get_my_name(name) :
    return name
my_name = get_my_name("자신의 이름")
print(my_name) # 출력 : 자신의 이름



# 원하는 수를 제곱해서 리턴해주는 함수를 만들어주세요, 그리고 num1 변수에 저장해주세요. num1을 출력해주세요.(매개변수, 리턴)

def square(num) :
    return num * num

num1 = square(4)
print(num1) # 출력 : 16

num2 = square(10)
print(num2) # 출력 : 100



# 원하는 수를 제곱한 후 2로 나눈 값을 리턴해주는 함수를 만들어주세요. 단, 제곱은 이미 만들어진 함수를 이용해야만 합니다. 제곱해주는 코드를 중복해서 사용하지 말아주세요. 변수에 저장해주세요. 그리고 변수를 출력해주세요.(매개변수, 리턴)

def my_calc(num) :
    return square(num) / 2 

num3 = my_calc(10)
print(num3) # 출력 : 50

num4 = my_calc(20)
print(num4) # 출력 : 200



# 1부터 임의의 수까지 사이에 있는 짝수들의 합을 리턴하는 함수를 만들어주세요. 마찬가지로 짝수 판벼 코드를 중복해서 작성하지 말고 이미 만들어진 짝수판별 함수를 이용해주세요. 그리고 변수에 저장해주세요. 변수를 출력해주세요.(매개변수, 리턴)

# 1부터 원하는 수까지의 짝수들의 합


# step 1. 1 ~ 10까지 출력
# step 2. 1 ~ 10까지의 합 출력
# step 3. 1 ~ 10까지의 짝수의 합 출력

def is_even(n) :
    if n % 2 == 0 :
        return True
    else :
        return False

def get_sum_of_even(num) :
    num1 = 0 
    for i in range(1, num+1) :
        if is_even(i) :
            num1 += i 
    return num1
        
    

        
      
            

num5 = get_sum_of_even(10)

print(num5) # 출력 :30 

num6 = get_sum_of_even(100)

print(num6) # 출력 :2550


# list1을 이용해 다음을 풀어주세요. 중복된 코드가 있어서는 안됩니다.

list1 = [2,3,6,6,7,3,32,24,23,54,687,1,24,324,112]



# list1의 모든 값의 합 (답 : 1308)

def sum_of_list(listn) :
    sum = 0

    for num in listn :
        sum += num 
    return sum    
    
# list1의 평균 (답 : 87.2)

def avg_of_list(listn) :
    avg = sum_of_list(listn) / len(listn)
    return avg

print(avg_of_list(list1))

# list1에서 평균 이상인 값만 출력 (답 : 687, 324, 112) 

def num_of_list(listn) :
    for num in listn :
        if avg_of_list(listn) <= num :
            print(num)
            
num_of_list(list1)
            
        
# 딕셔너리를 이용해서 회원 정보를 저장해주세요. 회원 정보는 아이디, 비밀번호, 이름으로 하겠습니다.
# 아이디가 hong123, 비밀번호가 1234, 이름이 홍길동인 회원
# 아이디가 sony7, 비밀번호가 7777, 이름이 손흥민인 회원
# 아이디가 ryu99, 비밀번호가 9999, 이름이 류현진인 회원

# 위 세명의 회원을 딕셔너리를 이용해 만들고 출력해주세요. 회원의 정보를 모두 출력해주세요.


'''
아이디 : hong123
비밀번호 : 1234
이름 : 홍길동
================
아이디 : sony7
비밀번호 : 7777
이름 : 손흥민
================
아이디 : ryu99
비밀번호 : 9999
이름 : 류현진
================

'''
dict1 = {"아이디" : 'hong123' , "비밀번호" : '1234', "이름" : '홍길동'}
dict2 = {"아이디" : 'sony7' , "비밀번호" : '7777', "이름" : '손흥민'}
dict3 = {"아이디" : 'ryu99' , "비밀번호" : '9999', "이름" : '류현진'}
print(dict1["아이디"])
print(dict2["아이디"])
print(dict3["아이디"])