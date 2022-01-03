#===============================
word1, num1 = input().split() #6036
print(word1 * int(num1))

#===============================
num1 = int(input())       #6037
word1 = input()
print(word1 * num1)

#================================
num1, num2 = input().split() #6038
print(int(num1) ** int(num2))

#==================================
num1, num2 = input().split() #6039
print(float(num1) ** float(num2))

#==================================
num1, num2 = input().split() #6040
print(int(num1) // int(num2))

#====================================
num1, num2 = input().split() #6041
print(int(num1) % int(num2))

#====================================
num = float(input())         #6042
print( format(num,".4f"))    # format(실수, ".nf")를 사용하면 
                             # 실수에 소수점 n+1에서 반올림해서 값이 나온다.

#=====================================                          
num1, num2 = input().split() #6043
num3 = float(num1) / float(num2)
print(format(float(num3),".3f")) 

#======================================
num1, num2 = input().split()  #6044
num1 = int(num1) 
num2 = int(num2)
num3 = num1 / num2
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)
print(format(float(num3),".2f"))

#============================================
num1, num2, num3 = input().split() #6045

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = num1 + num2 + num3 

print(num4, format(int(num4) / 3, ".2f"))
