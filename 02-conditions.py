# Conditional Flow

# if-elif-else structure

# if is mandatory, elif is optional [0, 1, ...N], else is optional [0, 1]
age = 65
# if age > 20:
#     if age > 60:
#         print("Senior")
#     print("Adult")
# elif age > 5:
#     print("Kid")
# else:
#     print("Baby")

if age > 60:
    print("Senior")

if age > 20:
    print("Adult")
elif age > 5:
    print("Kid")
else:
    print("Baby")

# Odd, Even problem
num = 6
# print("Odd")
# print("Even")
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Logical Operators - and, or and not
a, b, c, d = 5, 4, 3, 8
# Find the max - the easy way
if a > b and a > c and a > d:
    print(a)
elif b > a and b > c and b > d:
    print(b)
elif c > a and c > b and c > d:
    print(c)
else:
    print(d)

# better way to calculate maximum
max = b
if a > max:
    max = a
if c > max:
    max = c
if d > max:
    max = d
print(max)


a, b, c = 6, 7, 8
if (a+c>b) and (b+c>a) and (a+b>c):
    print("Valid")
else:
    print("Invalid")

# to check, whether a triangle is equilateral, isosceles, or scalene
if a == b and b == c and c == a:
    print("e")
elif a == b or b == c or c == a:
    print("i")
else:
    print("s")

# find the minimum of five numbers a, b, c, d, e
min= b
if a < min:
    min = a
if c < min:
    min = c
if d < min:
    min = d
if e < min:
    min = e
print(min)























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
