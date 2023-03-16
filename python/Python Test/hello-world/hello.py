print('Hello, World!')

# program.py
sum = 1 + 2
print(sum)

print("show this in the console")

#Variables
sum = 1 + 2 #3
product = sum * 2
print(product)

#Date Types - Solar System
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print(type(distance_to_alpha_centauri)) ## <class 'float'>

#Operators
left_side = 10
right_side = 5
total = (left_side / right_side) # 2
print(total)

total += 2
print(total)

total -= 1
print(total)

total /= 3
print(total)

total *= 5
print(total)

#Dates
from datetime import date
print(date.today())

print("Today's date is: " + str(date.today()))

print("1" + 2)