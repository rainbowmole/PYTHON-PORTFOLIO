#display
print('\t', '\t', '\t', ' Multiplication Table',)
for n in range(1, 10):
        print('\t', n, end="",)
print()
for d in range(45):
    print('-', end="")

#multiplication
#short version
for x in range(1, 10):
    print("\n", x, "|", end="")
    for y in range(1, 10):
            print( "\t", x * y, end="")
    print()