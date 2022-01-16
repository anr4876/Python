# 문제 : a와 b가 가지고 있는 값을 서로 뒤바꿔주세요.
# 조건 : 아래와 같이 출력 되도록 해주세요.

# 개념시작
# a라는 데이터 저장공간을 만들고 거기에 5를 집어 넣는다.
a = 5
print("a : {}".format(a))

b = 10
print("b : {}".format(b))
# 개념끝

c = b
b = a
a = c

# 문제시작
# 구현시작



# 구현끝
print("a : {}".format(a))
# 출력 => a : 10
print("b : {}".format(b))
# 출력 => b : 5

# 문제끝
n1 = 100

print(n1)

n2 = n1 + 10
print(n2)

n3 = n2 / 10
print(n3)

n4 = n3 - 10
print(n4)

n5 = n4 * 10
print(n5)
#============================================
# 변수활용
n1 = 100
print(n1)

n1 = n1 + 10
print(n1)

n1 = n1 / 10
print(n1)

n1 = n1 - 10
print(n1)

n1 = n1 * 10
print(n1)

#아래 코드를 변수를 이용해 간단하게 바꿔주세요.

n = 1
print(1)

n = n + 2 
print(n)

n = n + 3
print(n)

n = n + 4
print(n)

n = n + 5
print(n)

# 다른방법
num = 1
i = 1
print (num)
i = i + 1
num = num + i

print (num)
i = i + 1
num = num + i

print (num)
i = i + 1
num = num + i

print (num)
i = i + 1
num = num + i

print (num)
i = i + 1
num = num + i

# 1. 사용자로부터 2개의 실수를 입력받아 합계를 구하는 프로그램을 구현하시오. (hint : float() )

# 실행 예
# 첫번째 실수를 입력하세요 : 1.23
# 두번째 실수를 입력하세요 : 2.34
# 1.23와 2.34의 합은 3.57입니다.

num1 = float(input("첫번째 실수를 입력하세요 : "))
num2 = float(input("두번째 실수를 입력하세요 : "))
print(num1, '와', num2, '의 합은', num1 + num2, '입니다.') 

#다른방법
num1 = float(input("첫번째 실수를 입력하세요 : "))
num2 = float(input("두번째 실수를 입력하세요 : "))
print("{}와 {}의 합은 {}입니다.".format(num1, num2, num1 + num2))


# 홀수 짝수 판별하기
# 짝수는 2의 배수. 2의 배수는 2로 나누어 떨어지는 수.
# 홀수는 짝수가 아닌 경우가 홀수.
# 숫자 하나를 입력받습니다.
# 입력된 값이 홀수면 홀수 출력, 짝수이면 짝수 출력

## 입출력예시
# 숫자를 입력해주세요 : 10
# 10은 짝수입니다.

# 숫자를 입력해주세요 : 11
# 11은 홀수입니다.

# 숫자를 입력해주세요 : 37
# 37은 홀수입니다.

num1 = int(input("숫자를 입력해주세요 : "))
num2 = num1 % 2
if  num2 == 0 :
    print("{}은 짝수입니다.".format(num1))
if  num2 == 1 :
    print("{}은 홀수입니다.".format(num1))

   
# 두수를 입력받습니다.
# 두 수중 더 큰수에서 더 작은 수를 뺀 결과를 출력해주세요.
# num1, num2 두 값을 바꿔가면서 테스트해보세요.

## 입출력 예시
# 첫번째 숫자를 입력해주세요 : 10
# 두번째 숫자를 입력해주세요 : 20
# 20 - 10은 10입니다.

# 첫번째 숫자를 입력해주세요 : 30
# 두번째 숫자를 입력해주세요 : 10
# 30 - 10은 20입니다.

num1 = int(input("숫자를 입력해주세요 : "))
num2 = int(input("숫자를 입력해주세요 : "))

if num2 > num1 :
    num3 = num1
    num1 = num2
    num2 = num3

if num1 > num2 :
    print("{} - {}은 {}입니다.".format(num1,num2,num1 - num2))