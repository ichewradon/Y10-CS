from dataclasses import dataclass
@ dataclass

class Car:
    # below are fields that make record
    make:str
    model:str
    reg:str
    price:float
    no_of_doors:int

#intstantiating - creating an entry
my_car = Car ("BMW", "Isetta", "OE56 XFY", 15000.00, 1)

print ()
print ("===================================================================")
print (f"The car is a : {my_car.make}, {my_car.model}")
print ("===================================================================")


my_car.make = "Peel"
my_car.model = "P50"
my_car.no_of_doors= "2"
my_car.price = "27000.00"


print ()
print ("===================================================================")
print (f"The car is a : {my_car.make}, {my_car.model}.")
print (f"It has {my_car.no_of_doors} doors, the number plate is {my_car.reg} and it costs £{my_car.price}")
print ("===================================================================")
print ()
