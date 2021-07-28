# Main Part

num = int(input("Enter the number you want to find the divisors of: "))

num_until_num = range(1,num + 1)

divisors = []

for f in num_until_num:
    if num % f == 0:
        divisors.append(f)
    else:
        pass

print(divisors)