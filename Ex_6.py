# Main Part

is_palindrome = False

string = input('Enter the string that you want to check is whether a palindrome or not: ')

for i in range(1, len(string)):
    f = i+1
    if string[i] == string[-f]:
        is_palindrome = True
    else:
        pass

if is_palindrome != True:
    print(string, ' is not a palindrome.')
else:
    print(string, ' is a palindrome.')