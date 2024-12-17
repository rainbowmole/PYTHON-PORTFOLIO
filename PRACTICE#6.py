wwv = ""

u_w = str(input("Enter a word: "))
u_w = u_w.upper()

for l  in u_w:
    if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
        continue
    else:
        print(l, end=" ")

