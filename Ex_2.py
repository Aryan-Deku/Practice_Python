# Part 1 - Only even or odd with dividing with 4.

number = int(input("Enter the Number: "))

if number % 2 == 0:
    if number % 4 == 0:
        print(number, " is an even numer which is divisible by 4 and 2.")
    else:
        print(number," is an even number.")
else:
    print(number, " is an odd number.")

# Part 2 - To check with own number and divisor.

num = int(input("Enter the number you want to divide: "))
check = int(input("Enter the number you want to divide with: "))

if num % check == 0:
    print(num, " is divisible by ",check)
else:
    print(num, " is not divisible by ", check)