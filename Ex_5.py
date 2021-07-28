from random import randint

# Main Part

a = []
b = []
in_both = []

for l in range(1, 20):
    a.append(randint(0,50))
    b.append(randint(0,50))


for i in a:
    if i in b:
        in_both.append(i)
    else:
        pass

print(in_both)

# Extra 2
in_both2 = set([for i in a if i in b])
in_both2 = list(in_both2)
print(in_both2)