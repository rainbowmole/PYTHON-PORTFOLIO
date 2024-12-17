import datetime
import os

class PatientRecord:
    def __init__(self, filename="patients.txt"):
        self.filename = filename

    def get_existing_patient_ids(self):
        if not os.path.exists(self.filename):
            return set()

        with open(self.filename, "r") as file:
            patients = file.readlines()

        existing_ids = set()
        for patient in patients:
            if patient.strip():
                patient_id, *_ = patient.strip().split(", ", 1)
                existing_ids.add(patient_id)

        return existing_ids

    def add_patient(self):
        existing_ids = self.get_existing_patient_ids()
        patient_id = input("Register patient id: ")

        if patient_id in existing_ids:
            print("Patient ID already exists. Please use a unique ID.")
            return

        patient_name = input("Enter patient's name: ").title()
        medicine = input("Enter medicine to take: ").title()
        medicine_date = input("The medicine should be taken every (Mon/Tues/Wed/Thurs/Fri/Sat/Sun)?: ").title()
        medicine_time = input("The medicine should be taken at (HH:MM:SS): ")
        try:
            medicine_time = datetime.datetime.strptime(medicine_time, '%H:%M:%S')
        except ValueError:
            print("Invalid time format. Please enter time as HH:MM:SS.")
            return

        with open(self.filename, "a") as file:
            file.write(f"{patient_id}, {patient_name}, {medicine}, {medicine_date}, {medicine_time.strftime('%H:%M:%S')}\n")

        print("Patient added successfully!")

    def view_patients(self):
        if not os.path.exists(self.filename):
            print("FILE NOT FOUND")
            return

        patients = {}

        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                if len(parts) == 5:
                    patient_id, patient_name, medicine, medicine_date, medicine_time = parts
                    if patient_id in patients:
                        patients[patient_id].append((patient_name, medicine, medicine_date, medicine_time))
                    else:
                        patients[patient_id] = [(patient_name, medicine, medicine_date, medicine_time)]

        print("\n ALL PATIENTS ")

        for patient_id, patient_list in patients.items():
            print(f"\nPatient ID: {patient_id}")
            for patient_name, medicine, medicine_date, medicine_time in patient_list:
                print(f"\tPatient's Name: {patient_name}"
                      f"\n\tMedicine taking: {medicine}"
                      f"\n\tTaking every: {medicine_date} at {medicine_time}\n")

    def view_patients_by_id(self):
        if not os.path.exists(self.filename):
            print("FILE NOT FOUND")
            return

        patients = {}

        with open(self.filename, "r") as file:  # Open the file in read mode
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                if len(parts) == 5:
                    patient_id, patient_name, medicine, medicine_date, medicine_time = parts
                    if patient_id in patients:
                        patients[patient_id].append((patient_name, medicine, medicine_date, medicine_time))
                    else:
                        patients[patient_id] = [(patient_name, medicine, medicine_date, medicine_time)]

        patient_id = input("Enter the patient id you want to view: ").title()
        filtered_patients = patients.get(patient_id, [])

        if not filtered_patients:
            print(f"Patient does not exist")
        else:
            print(f"\nPatient {patient_id}")
            for patient_name, medicine, medicine_date, medicine_time in filtered_patients:
                print(f"\tPatient's Name: {patient_name}"
                      f"\n\tMedicine: {medicine}"
                      f"\n\tTaking every: {medicine_date} at {medicine_time}\n")

def main():
    filename = "patients.txt"
    record = PatientRecord(filename)

    print("\nWelcome to Patient's Medicine Tracker")
    while True:
        print("\n1. Add patient")
        print("2. View All patients")
        print("3. View patient by their ID")
        print("4. Exit\n")

        choice = input("Please enter your choice: ")

        if choice == '1':
            record.add_patient()
        elif choice == '2':
            record.view_patients()
        elif choice == '3':
            record.view_patients_by_id()
        elif choice == '4':
            print("\nThank you for your hard work")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.\n")

if __name__ == '__main__':
    main()

