# For loops
#
# # print first 100 natural numbers
# for i in range(1, 101):
#     if i < 100:
#         print(i, end=",")
#     else:
#         print(i)
#
# # print square of first 100 natural numbers
# for num in range(1, 101):
#     print(num**2, end=",")
# print()
    
# # print "hello world" 10 times
# for i in range(10):
#     print("Hello World") #This will print 'Hello World' 10x times and i from 0 to 9 as index initialize from 0
#     print(i)
#
# # print even numbers in [2, 100]
# for i in range(2, 101):
#     if i % 2 == 0:
#         print(i, end=", ")
# print()
#
# # multiples of 13 between [100, 200]
# for num in range(100, 201):
#     if num % 13 == 0:
#         print(num, end=",")  #We are using end="," to make the consecutive output in the same line and not next line
# print()
# print("-"*20)

# check if a number is prime or not
num = 7
result = True
for i in range(2, int(num**2)+1):
    if num % i == 0:
        result = False
print(result)

# how to take input from user
output = int(input("Enter  number: "))
print(output*2)

output = int(input("Enter a number: "))
i = 0
while i<=output:
    print(i)
    i = i + 1























    
    
    
    
    
    
    
    
    
    
    
    