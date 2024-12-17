#Display
print('------------------------------------------------------------')
print("PLEASE CHOOSE AN ACTION:")
print("ACTION [1] Determine if the number is +,-,0")
print("ACTION [2] Determine if number is ODD or EVEN")
print("ACTION [3] Determine if the letter is VOWEL/CONSONANT", '\n')

#input
choice = int(input("Enter your choice [1] [2] [3]: "))

#CHOICE 1
print()
if choice == 1:
    n = int(input("Enter a number: "))
    if n < 0:
        print("The number is negative")
    elif n == 0:
        print("The number is zero")
    else:
        print("The number is positive")
#CHOICE 2
print()
if choice == 2:
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

#CHOICE 3
print()
if choice == 3:
    l = str(input("Enter a letter: "))
    if (l == 'A' or l == 'a' or
            l == 'E' or l == 'e' or
            l == 'I' or l == 'i' or
            l == 'O' or l == 'o' or
            l == 'U' or l == 'u'):
        print("The letter is a vowel")
    else:
        print("The letter is a consonant")

#INVALID CHOICE
if choice > 3:
    print("Invalid Input")

print("------------------------------------------------------------")
