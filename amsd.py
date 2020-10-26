# This program asks users for 2 numbers and then performs add/sub/mul/div based on user response

# Addition
def numadd(num1, num2):
    tot = num1 + num2
    return tot

# Substraction
def numsub(num1, num2):
    tot = num1 - num2
    return tot

# Multiplication
def nummul(num1, num2):
    tot = num1 * num2
    return tot

# Division
def numdiv(num1, num2):
    tot = num1 / num2
    return tot

print ("Play with numbers..........")
num1 = int(raw_input ("Enter num1: "))
num2 = int (raw_input ("Enter num2: "))
choice = raw_input ("Which arithmetic operation would you like to perform?  ")

if choice == "+":
    print ("Your result is: "), (numadd(num1, num2))

elif choice == "-":
    print ("Your result is: "), (numsub(num1, num2))

elif choice == "*":
    print ("Your result is: "), (nummul(num1, num2))

elif choice == "/":
    print ("Your result is: "), (numdiv(num1, num2))

else:
    print ("Your choice of arithmetic operation is not valid.....")

