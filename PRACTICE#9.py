ones = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "]
teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", 'Fifteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ["", 'Ten', "twenty", 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
ta = 'Y'

while ta == 'Y':
    num = int(input("Enter a number ranging from 0 to 9999: "))
    if num == 0:
        print("zero")
    else:
        if num >= 1000:
            print(ones[num//1000] + "Thousand", end=" ")
            num %= 1000

        if num >= 100:
            print(ones[num//100] + "Hundred", end=" ")
            num %= 100

        if num >= 20 or num == 10:
            print(tens[num//10], end=" ")
            num %= 10

        if num < 20 and num > 10:
            print(teens[num%10], end=" ")

        if num < 10:
            print(ones[num//1], end=" ")

    print()
    ta = input("Another try?: ")
    ta = ta.upper()

    if ta == 'Y':
        ones = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "]
        teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", 'Fifteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ["", 'Ten', "twenty", 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
