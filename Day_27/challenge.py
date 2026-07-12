def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(add(2,7,5,8,9,3))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_Car = Car(make='Opel', model='corsa')
print(my_Car.make)
print(my_Car.model)