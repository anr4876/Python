# 문제 : 자동차가 3번 달리게 해주세요.
# 출력 : 자동차가 달립니다.

# v1. 1개의 자동차가 3번 달리게 해주세요.

# v2. 3개의 자동차가 1번씩 달리게 해주세요.

# 자동차가 달립니다.
# 자동차가 달립니다.
# 자동차가 달립니다.
# 자동차가 달립니다.
# 자동차가 달립니다.
# 자동차가 달립니다.

class carr :
    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
    
    def car_number(self) :
        print("{}개의 자동차가 {}번 달리게 해주세요.".format(self.num1, self.num2))
    
    def car_gogo(self) :
        for i in range(self.num1) :
            for x in range(self.num2) :
                print("자동차가 달립니다.")
        
        
        
car1 = carr(1, 3)
car2 = carr(3, 1)


car1.car_number()
car2.car_number()

car1.car_gogo()
car2.car_gogo()

#================================================================================================
# 문제 : 자동차 객체를 담을 변수를 만들어주세요.
# 자동차 객체를 변수에 담고 그 변수를 이용해 최고속력이 서로 다르게 만들어주세요.

# 각 자동차가 자신의 최고속력으로 달리게 해주세요.


# 출력 : 자동차가 최대속력 220km로 달립니다.
# 출력 : 자동차가 최대속력 250km로 달립니다.

class speedcar :
    def __init__(self, fullpower) :
        self.fullpower = fullpower
        
    def car_run(self) :
        print("자동가사 최대속력 {}km로 달립니다.".format(self.fullpower))
        
        
speed1 = speedcar(220)
speed2 = speedcar(250)

speed1.car_run()
speed2.car_run()

# ==========================================================================================================


# 다음 코드가 동작하도록 class를 완성해주세요

class person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        
    def introduce(self) :
        print("안녈하세요 {}살 {}입니다.".format(self.age, self.name))  
        
class car :
    def __init__(self, name, color, speed) :
        self.name = name
        self.color = color
        self.speed = speed
        
    def drive(self) :
        print("{} {}이/가 {}로 달립니다.".format(self.color, self.name, self.speed))   

p1 = Person("홍길동", 27)
p2 = Person("홍길순", 25)

p1.introduce() # 안녕하세요 27살 홍길동입니다.
p2.introduce() # 안녕하세요 25살 홍길순입니다.

c1 = Car("소나타", "하얀색", 100)
c2 = Car("모닝", "검정색", 70)

c1.drive() # 하얀색 소나타이/가 100km로 달립니다.
c2.drive() # 검정색 모닝이/가 70km로 달립니다.

# cat1 = Cat("아리", "러시안블루", 4)
# cat2 = Cat("망고", "샴", 6)

# cat1.meow() # 4살 러시안블루 고양이 아리가 야옹하고 웁니다.
# cat2.meow() # 6살 샴 고양이 망고가 야옹하고 웁니다.



# w1 = Warrior("이순신", 20, 10)
# w2 = Warrior("강감찬", 15, 15)

# w1.status() # 이름 : 이순신, 공격력 : 20, 방어력 : 10 
# w2.status() # 이름 : 강감찬, 공격력 : 15, 방어력 : 15 

# w1.attack() # 이순신이 20의 데미지를 입힙민다.
# w2.attack() # 강감찬이 15의 데미지를 입힙민다. 

# w1.defense() # 이순신이 10 데미지를 방어합니다.
# w2.defense() # 강감찬이 15 데미지를 방어합니다.



