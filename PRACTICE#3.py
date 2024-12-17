#input
l = str(input("Enter a letter: "))

#process
if (l == 'A' or l == 'a' or
        l == 'E' or l == 'e' or
        l == 'I' or l == 'i' or
        l == 'O' or l == 'o' or
        l == 'U' or l =='u'):
#output
    print("vowel")
else:
    print("Consonant")