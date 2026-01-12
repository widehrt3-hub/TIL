#1
age = 21
#2
height = 177.9
#3
complex_num = 1 + 2j
#4
base = float(input("Enter base :"))
height = float(input("Enter height :"))
area = 0.5 * base * height
print("The area of the triagle is", area)
#5
side_a = float(input("Enter side a :"))
side_b = float(input("Enter side b :"))
side_c = float(input("Enter side c :"))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)
#6
length = float(input("Enter lenght :"))
width = float(input("Enter width :"))
area = length * width
perimeter = 2 * (length + width) 
print("Area :", area)
print("Perimeter :", perimeter)
#7
radius = float(input("Enter radius :"))
pi = 3.14
area = pi * radius * radius
circumference 2 * pi * radius
print("Area :", area)
print("Circumference :", circumference)
#8
slope = 2
x_intercept = 1
y_intercept = -2
print(slope, x_intercept, y_intercept)
#9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1)/(x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Slope :", slope)
print("Distance :", distance)
#10
if 2 > slope:
  print("8>9")
elif 2 < slope:
  print("8<9")
else:
  print("Equal")
#11
for x in range(-6, 1):
  y = x**2 + 6*x + 9
  print(x, y) #(-3, 0)
#12
print(len("python") != len("dragon"))
#13
print("on" in "python" and "on" in "dragon")
#14
print("jargon" in "I hope this course is not full of jargon.")
#15
print(not("on" in "python" and "on" in "dragon"))
#16
length_1, length_2 = len("python"), len("dragon")
print(float(length_1), str(length_1), float(length_2), str(length_2))
#17
num = int(input("Enter number :"))
print(num % 2 == 0)
#18
print((7 // 3) == int(2.7))
#19
print(type('10') == type(10))
#20
print(int(float('9.8')) == 10)
#21
hours = float(input("Enter hours :"))
rate = float(input("Enter rate per hour :"))
pay = hours * rate
print("Your weekly earning is", pay)
#22
years = float(input("Enter number of years you have lived :"))
seconds = 60 * 60 * 24 * 365 * years
print("You have lived for", seconds, "seconds.")
#23
for x in range(1, 5):
  print(x, x**0, x**1, x**2, x**3)










# 1. The role of a comma in the function print : to change value into string and add a blank between. => print("The area of the triagle is", area)
# 2. To define a variable, don't use - rather than _. ex) x-intercept(X), x_intercept(O)
# 3. print(8>9) -> False, print(8 ">" 9) -> error, print(8, ">", 9) -> 8 > 9
# 4. In Python, the and operator performs a logical evaluation but returns the last evaluated operand: it returns A if A is False, otherwise it returns B. => print("on" in "python" and "dragon") -> dragon, print("on" in "python and "on" in "dragon") -> True
# 5. int('9.8') -> error, int(float('9.8')) -> 9
# 6. range(1,6) means 1~5




