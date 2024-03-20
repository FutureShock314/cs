from dataclasses import dataclass

@dataclass
class Person:
  name: str
  name2: str
  age: int

  def unborn(self):
    print('ok')
    self.age = -10

p = Person('John', 'Doe', 30)
print(p)
p.unborn()
print(p)
