import calendar
import datetime

def age_calculator(birthyear, birthmonth, birthday):
    present_year = datetime.datetime.now().year
    present_month = datetime.datetime.now().month
    present_day = datetime.datetime.now().day

    user_age = present_year - birthyear - ((present_month, present_day) < (birthmonth, birthday))

    return user_age

def leapYearCon(lyear):
    if calendar.isleap(lyear) == True:
        print(lyear, "is a leap year")
    else:
        print(lyear, "is not  a leap year")

def GenMonth(year, month):
    print(f" Calendar for {calendar.month(year, month, 2).strip(" ")}\n")

def IterateMonth(startingdate):
    days31 = [1,3,5,7,8,10,12]
    days = startingdate.split('-')
    year =  int(days[0])
    month =  int(days[1])
    date =  int(days[2])

    three1 = 31 - date
    three0 = 30 - date

    if month in days31:
        for i in range(three1):
            date += 1
            print(f"{year}-{month}-{date}")
    elif month not in days31:
        for a in range(three0):
            date += 1
            print(f"{year}-{month}-{date}")

def main():
    while True:
        print("\nWelcome to Calendar Function Demo\n")
        print("Choose an option: \n"
              "1. Age Calculator \n"
              "2. Check if a year is a leap year \n"
              "3. Generate a calendar for a specific month \n"
              "4. Iterate over date in a month \n"
              "5. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            print('\nAGE CALCULATOR\n')
            birthyear = int(input("Enter your birth year: "))
            birthmonth = int(input("Enter your birth month: "))
            birthday = int(input("Enter your birth day: "))
            age = age_calculator(birthyear, birthmonth, birthday)
            print(f"You're currently {age} years old")
        elif choice == '2':
            print("\nLEAP YEAR CONFIRMATION\n")
            lyear = int(input("Enter a year: "))
            leapYearCon(lyear)
        elif choice == '3':
            print("\nCALENDAR \n")
            year = int(input("Enter the year: "))
            month = int(input("Enter the month: "))
            GenMonth(year, month)
        elif choice == '4':
            print("\nDATE ITERATOR\n")
            startingdate = input("Enter starting date (YYYY-MM-DD): ")
            IterateMonth(startingdate)
        elif choice == '5':
            print("\nExiting the program....")
            break
        else:
            print("\nPlease try again..")

if __name__ == '__main__':
    main()