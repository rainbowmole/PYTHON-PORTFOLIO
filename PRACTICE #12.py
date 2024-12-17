print("------LAZY COLLATZ SEQUENCE (´。＿。｀)--------")
print()
def collatz(num):
    lst = []
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
        lst.append(num)
    else:
        print(lst)
        print('Done (o゜▽゜)o☆!')


def main():
    ta = 'Y'
    while ta == 'Y':
        num = int(input('Enter a number: '))
        collatz(num)
        print()
        ta = input("Wanna try again (oﾟvﾟ)ノ[Y|N]: ")
        ta = ta.upper()
        if ta == 'Y':
            print()
        else:
            print("Until next time o(TヘTo)")


main()