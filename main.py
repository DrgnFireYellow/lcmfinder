from sympy import lcm
from rich import print

num1 = int(input("Enter the first number to find LCMs for> "))
num2 = int(input("Enter the second number to find LCMs for> "))
first_result = lcm(num1, num2)
result = first_result
print(first_result)
keep_going = input("Would you like to find the next LCM? [y/n] ")

if keep_going.lower().startswith("y"):
    keep_going = True
elif keep_going.lower().startswith("n"):
    keep_going = False

while keep_going:
    result = result + first_result
    print(result)
    keep_going = input("Would you like to find the next LCM? [y/n] ")

    if keep_going.lower().startswith("y"):
        keep_going = True
    elif keep_going.lower().startswith("n"):
        keep_going = False
