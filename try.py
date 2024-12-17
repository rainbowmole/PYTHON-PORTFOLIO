import datetime
import os

class Patient_record:
    def __init__(self, filename):
        self.filename = filename

    def add_patient(self):
        patient_id = input("Register patient's id: ")
        name = input("Enter patient's name: ").title()
        admission = input("Admitted due to: ")
        contact_details = input("Enter guardian's contact details: ")

        with open(self.filename, "a") as file:  # Open the file in append mode
            file.write(f"{patient_id}, {name}, {admission}, {contact_details}\n")

        print("Patient added successfully!")

    def view_patients(self):
        if not os.path.exists(self.filename):  # Check if file exists
            print("FILE NOT FOUND")  # Print message if file doesn't exist
            return

        with open(self.filename, "r") as file:
            patients = file.readlines()

        if not patients:  # Check if the file is empty
            print("WOW ALL PEOPLE AROUND YOU SEEM HEALTHY")
            return

        print("\nPatient List:\n")
        for patient in patients:
            patient_id, name, admission, contact_details = patient.strip().split(", ")

            print(f"Patient\'s ID: {patient_id} "
                  f"\nPatient\'s Name: {name} "
                  f"\nReason: {admission} "
                  f"\nGuardian\'s Contact: {contact_details}\n")

class Medicine_tracker:
    def __init__(self, filename):
        self.filename = filename
        self.schedule = []

    def add_medicine(self, patient, medicine, medicine_schedule):
        self.schedule.append({"Patient": patient, "Medicine": medicine, "Time to take": medicine_schedule})
        print("Medicine added successfully!")

    def view_schedule(self):
        if not self.schedule:
            print("No medicine schedule found.")
            return

        print("Medicine Schedule:")
        for entry in self.schedule:
            print(f"Patient: {entry['Patient']}, "
                  f"Medicine: {entry['Medicine']}, "
                  f"Time to take: {entry['Time to take']}")

def main():
    patient_filename = "patients.txt"
    medicine_filename = "medicine_tracker.txt"

    patient_manager = Patient_record(patient_filename)
    medicine_manager = Medicine_tracker(medicine_filename)

    while True:
        print("\nMedicine Tracker")  # Display menu options
        print("1. Add patient")
        print("2. View patients")
        print("3. Add medicine")
        print("4. View medicine schedule")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_manager.add_patient()
        elif choice == '2':
            patient_manager.view_patients()
        elif choice == '3':
            patient = input("Enter patient id: ")
            medicine = input("Enter medicine name: ")
            medicine_time = input("When should the medicine be taken (YYYY-MM-DD HH:MM:SS): ")
            medicine_time = datetime.datetime.strptime(medicine_time, '%Y-%m-%d %H:%M:%S')
            medicine_schedule = medicine_time.strftime('%B %d, %Y %I:%M %p')
            medicine_manager.add_medicine(patient, medicine, medicine_schedule)
        elif choice == '4':
            medicine_manager.view_schedule()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
