# 출력

print(100)
print(2 + 2)
print(12 - 10)



# 문자 출력

#print(연성묵) 
print('연성묵')
print("연성묵")
print('200' + '200') #200을 문자로 표기
# '' => 문자형
# '' 안붙고 숫자만 => 숫자형


# 주석 - 파이썬 명령어가 아닌, 메모 
# 주석 종류 #
'''문장 전체주석'''
# 전부 주석처리할때 드래그한후 컨트롤 + 물음표(슬래시)


print('1 + 2 = 4')


# 형변환

# 문자(str), 숫자(int)
print(int('1') + int('1'))

# 숫자를 문자로
print(str('1') + str('1'))
print('11231 + 34342 = ' + str(11231 + 34342))

# 문자에는 포맷 기능이 있음.
print('{} + {} = {}'.format(4, 6, 4 + 6))

#==========================================================================

# 데이터를 재사용하기 위해서 저장
# 변수에 저장
# 변수 -> 상자
# 변수명 -> 상자이름

num1 = 26
num2 = 32


print(num1) # num1을 변수명으로 본다
print('num1') # num1을 문자로 본다
print(num2)
print('num2')

print('{} + {} = {}'.format(num1, num2, num1 + num2))

name = "연성묵"
print('{}'.format(name))



















