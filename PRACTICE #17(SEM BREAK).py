print("Employee's Salary Calculator", '\n')
id = input("Please Enter Employee's ID Number: ")
rate = float(input("Employee's rate per hour: "))
def formula():
    days = float(input("Enter number of days you worked for 2 weeks: "))
    hoursworked = days * 24
    gp = rate * hoursworked

    tax = .20 * gp
    sss = .05 * gp
    ph = 150
    pi = 150

    td = tax + sss + ph + pi

    netpay = gp - td

    print()
    print("You\'re Employee Number:", id)
    print('\t', "Gross pay:", gp)
    print('\t', "Total Deduction from tax, sss, philhealth, and pag ibig:", td)
    print('\t', "You\'re next salary is", netpay)

formula()
