class Person :
  def __init__(self, name, age) :
    self.name = name
    self.age = age
  
  def introduce(self) :
    print("안녕하세요 {}살 {}입니다.".format(self.age, self.name))

class Car :
  def __init__(self, model, velo) :
    self.model = model
    self.velo = velo
  
  def drive(self) :
    print("{}이/가 {}km로 주행합니다.".format(self.model, self.velo))