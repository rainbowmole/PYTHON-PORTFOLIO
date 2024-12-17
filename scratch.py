import datetime
def add_medicine():
    patient_id = input("Register patient id: ")
    patient_name = input("Enter patient\'s name: ").title()
    medicine = input("Enter medicine to take: ").title()
    medicine_time = input("When should the medicine be taken (YYYY-MM-DD HH:MM:SS): ")
    medicine_time = datetime.datetime.strptime(medicine_time, '%Y-%m-%d %H:%M:%S')
    medicine_schedule = medicine_time.strftime('%B %d, %Y %I:%M %p')

    print("\npatient added successfully! \n")
    print(f"Patient\'s Id: {patient_id} "
          f"\n\t Name: {patient_name}  "
          f"\n\t Medicine: {medicine} | "
          f"Time to take: {medicine_schedule}\n")

def main():
    print("\nWelcome Patient's Medicine Tracker")
    while True:
        print("\n1. Add patient")
        print("2. Exit\n")

        choice = input("Please enter your choice: ")

        if choice == '1':
            add_medicine()

        elif choice == '2':
            print("\nThank you for your hardwork")
            break

        else:
            print("\nInvalid choice. Please enter a valid option.\n")

if __name__ == '__main__':
    main()




