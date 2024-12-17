def main():
    print("[1] Factorial of a number")
    print("[2] Compute Average")
    print("[3] EXIT")
def average():
    lst = []
    sum = 0
    for a in range(num2):
        user_in = int(input("Enter Number: "))
        lst.append(user_in)
        sum += lst[a]
    print("Average is ", sum/num2)
ta = 'Y'
while ta == 'Y':
    main()
    choice = int(input("Enter your choice [1|2|3]: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            else:
                return (num * factorial(num - 1))
        result = factorial(num)
        print("The factorial of", num, "is", result)

    if choice == 2:
        num2 = int(input("How many numbers?: "))
        average()

    if choice == 3:
        break

    print()
    ta = input("Try Again? [Y|N]: ")
    ta = ta.upper()
    if ta == 'Y':
        print()
