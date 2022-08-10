class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

logging.debug(p1.name)
logging.debug(p1.age)
