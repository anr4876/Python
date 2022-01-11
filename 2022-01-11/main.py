# 내장 모듈 - 파이썬 설치 할 때 이미 존재하는 모듈들
import math as m 
# math 모듈은 수학에 관한 다양한 기능을 모아놓은 모듈. 
# 모듈을 사용할 때는 import 라는 문법을 사용
# 모듈명이 길거나 다른 식별자와 겹칠 경우 as를 이용해 별칭을 지을 수 있음
print(m.pow(10, 2)) # 모듈 사용법. 모듈명(별칭).기능()
print(m.ceil(2.7))

# 사용자 모듈 - 사용자가 직접 만든 모듈
import my_math as mm # my_math.py 파일로 모듈 생성

print(mm.pow(2, 3))
print(mm.plus(2, 3))

import my_classes as mc

p1 = mc.Person("홍길동", 27)
p1.introduce()
p2 = mc.Car("소나타", 120)
p2.drive()
