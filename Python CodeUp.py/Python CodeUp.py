
print('Hello') 
print('World')
print("'Hello'")
print('"Hello World"')
print('\"!@#$%^&*()\'') # '를 출력하려면 \'를 이용해야한다
print('\"C:\\Download\\\'hello\'.py\"') # \를 출력하려면 \\를 써야한다.
print("print(\"Hello\\nWorld\")") # 줄바꿈도 \를 앞에 하나 더 써야한다.

#===================================
c = input()                    #6009
print(c)      # input은 지정한 상자 안에 사용자가 원하는것을 넣을때 쓰임

#===================================
n = int(input())               #6010
print(n)      # 형변환 안에  input을 넣어도 실행 가능 (코드를 줄일때 편함)

#===================================
f = float(input())             #6011
print(f)

#===================================
a = input()                    #6012
b = input()
print(a)
print(b)

#===================================
a = input()                    #6013
b = input()
print(b)
print(a)

#===================================
f = float(input())             #6014
print(f)            #float은 실수 형변환 함수이다.     
print(f)
print(f)

#===================================
a, b = input().split()         #6015
print(a)            #split()은  ()안에 있는 문자를 기준으로 잘라주는 함수이다.
print(b)            #split앞에 있는 .은 클래스와 객체안의 함수나 변수에 접근하는 연산자이다. 

#===================================
a, b = input().split()         #6016
print(a, b)

#===================================
s = input(s)                   #6017 
print(s,s,s)

#===================================
a,b = input().split(':')       #6018
print(a,b,sep=':')

#===================================
y, m, d = input().split('.')   #6019  
print(y, m, d, sep='-')

#===================================
f, h = input().split('-')      #6020
print(f, h, sep='')  # python에서 ,는 공백처리이다. 공백 없이 출력하려면
                     # sep=''안에 아무것도 넣지 않으면 공백 없이 출력된다.

#===================================                 
s = input()                    #6021
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#===================================
s = input()                    #6022
print(s[0:2], s[2:4], s[4:6])

#===================================
h, m, s = input().split(':')   #6023
print(m)

#===================================
w1, w2 = input().split()       #6024    
s = w1 + w2
print(s)

#===================================
num1, num2 = input().split()   #6025
num3 = int(num1) + int(num2)
print(num3)

#===================================
num1 = float(input())          #6026
num2 = float(input())
print(num1 + num2)

#===================================
num1 = input()                 #6027
num2 = int(num1)
print('%x' % num2)

#===================================
num1 = input()                 #6028
num2 = int(num1)
print('%X' %num2)

#===================================
num1 = input()                 #6029
num2 = int(num1, 16)
print('%o' % num2)

#===================================
num1 = ord(input())            #6030
print(num1)

#===================================
num1 = int(input())            #6031
print(chr(num1))

#===================================
num1 = int(input())            #6032
print(-num1)

#===================================
num1 = ord(input())            #6033
num1 += 1
print(chr(num1))

#===================================
num1, num2 = input().split()   #6034
num3 = int(num1) - int(num2)
print(num3)

#===================================
num1, num2 = input().split()   #6035
num3 = float(num1)*float(num2)
print(num3)