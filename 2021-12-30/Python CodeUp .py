print('Hello') 
print('World')
print("'Hello'")
print('"Hello World"')
print('\"!@#$%^&*()\'') # '를 출력하려면 \'를 이용해야한다
print('\"C:\\Download\\\'hello\'.py\"') # \를 출력하려면 \\를 써야한다.
print("print(\"Hello\\nWorld\")") # 줄바꿈도 \를 앞에 하나 더 써야한다.

#=======================================
c = input()                       #6009
print(c)      # input은 지정한 상자 안에 사용자가 원하는것을 넣을때 쓰임

#=======================================
n = int(input())                  #6010
print(n)      # 형변환 안에  input을 넣어도 실행 가능 (코드를 줄일때 편함)

#=======================================
f = float(input())                #6011
print(f)

#=======================================
a = input()                       #6012
b = input()
print(a)
print(b)

#=======================================