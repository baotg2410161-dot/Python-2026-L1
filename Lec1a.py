#ex1
r = int (input ("Enter a number: "))
pi = 3.14
print (" the area of the circle is: ", pi * r * r)

#ex2
a = float(input("Enter the temperature in Celsius: "))
print ("The temperature in Fahrenheit: ", a * 9/5 + 32)

#ex3
n = int(input("Enter a number? "))

if n < 2 or (n % 2 == 0 and n != 2):
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")

#ex4
n = int(input("Enter a number? "))
sum = 0
for i in range (1, n):
    if n % i == 0 :
        sum = sum + i
if sum == n :
  print (n, "is a perfect number")
else:
  print (n, "is not a perfect number")

#ex5
a= str(input("Enter your favorite color? ") )
color=["Red", "Blue", "White"]
if a in color:
    print("Your favorite color is at index", str(color.index(a)), "in my list")
else:
    print("Sorry, I could not find your color")

#ex6
print("range1 =", list(range(7))) 
print("range2 =", list(range(1, 11, 3))) 
print("range3 =", list(range(5,0, -1)))
print("range4 =", list(range(6, -4, -2)))

#ex7
def remove_dolar_sign(s): 
    return s.replace('$', '')
print(remove_dolar_sign('$100'))  

#ex8
def extract_even (I):
    return [x for x in I if x % 2 == 0]
s = input ("Enter the list of numbers:")
numbers = [int(x) for x in s.split()]
print(extract_even(numbers))

#ex9
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

number = int(input("Enter a non-negative integer: "))
print("Factorial:", factorial(number))

#ex10
def get_divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

number = int(input("Enter a number: "))
get_divisors(number)

#ex11
import math

def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

print("Distance:", distance(x1, y1, x2, y2))

#ex12
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")

print_pattern(3, 5)
