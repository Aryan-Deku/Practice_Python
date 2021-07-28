# Main Question

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a :
    if i < 5:
        print(i)
    else:
        pass

# Extra 1

arr = []

for i in a :
    if i < 5:
        arr.append(i)
    else:
        pass

print(arr)

# Extra 2

arr_2 = [x for x in a if x < 5]

print(arr_2)

# Extra 3

arr_3 = []

num = int(input("Enter the number to input from: "))
for f in a:
    if f < num:
        arr_3.append(f)
    else:
        pass

print(arr_3)