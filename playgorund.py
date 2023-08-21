def add(*args):
    print(args[4])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 5, 6, 7, 8, 91, 10, 11))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.price = kwargs.get('price')


my_car = Car(make="nissan", model='gtr')
print(my_car.model, my_car.make)
