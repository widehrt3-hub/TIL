# Day 2: 30 Days of python programming
first_name = 'Seongju'
last_name = 'Kim'
full_name = 'Seongju Kim'
country = 'South Korea'
city = 'Changwon'
age = 21
year = 2026
is_married = False
is_true = False
is_light_on = True
first_name, last_name, full_name = 'Seongju', 'Kim', 'Seongju Kim'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))

print(len(first_name) > len(last_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two

diff = num_one + num_two

product = num_one * num_two

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

radius = 30
pi = 3.141592
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print(area_of_circle)
print(circum_of_circle)

radius = float(input("Enter radius :"))
pi = 3.141592
area_of_circle = pi * radius ** 2
print(area_of_circle)

first_name = input("First name: ")
last_name = input("Last name: ")
country = input("Country: ")
age = int(input("Age: "))

print(first_name, last_name, country, age)

help('keywords')







# 1. quote(') in the result of print of dictionary is just the sign of the computer(python) to express that is a word. =>
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
print(person_info)

=>{'firstname': 'Asabeneh', 'lastname': 'Yetayeh', 'country': 'Finland', 'city': 'Helsinki'} (O)
{firstname: Asabeneh, lastname: Yetayeh, country: Finland, city: Helsinki}(X) 

# 2. zip(the built-in function) does not have any value but is likely a machine that creates values when we order using list, tuple or something else. So the result of print(zip(a,b)) is <zip object at 0x79ca4f705b40> which is the adress of zip machine.

# 3. print(type(first_name, last_name, full_name)) -> error. cause the function 'type' can only include one factor. So 'print(type((first_name, last_name, full_name)))' does not cause any error, but the result is tuple.

# 4. the type of the function 'input()' is always string.
