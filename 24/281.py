from collections import namedtuple

Engine = namedtuple('Engine', ['type', 'cylinders'])

Car = namedtuple('Car', ['make', 'model', 'year', 'engine'])

engine_instance = Engine(type='1.5L', cylinders=4)

car_instance = Car(make='Honda', model='City', year=2020, engine=engine_instance)

print("Car Make:", car_instance.make)
print("Car Model:", car_instance.model)
print("Car Year:", car_instance.year)
print("Car Engine Type:", car_instance.engine.type)
print("Car Engine Cylinders:", car_instance.engine.cylinders)