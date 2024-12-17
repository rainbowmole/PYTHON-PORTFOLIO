import datetime
import os

class PatientRecord:
    def __init__(self, patientfilename="patients.txt"):
        self.patientfilename = patientfilename

    def get_existing_patient_ids(self):
        if not os.path.exists(self.patientfilename):
            return set()

        with open(self.patientfilename, "r") as file:
            patients = file.readlines()

        existing_ids = set()
        for patient in patients:
            if patient.strip():
                patient_id, *_ = patient.strip().split(", ", 1)
                existing_ids.add(patient_id)

        return existing_ids

    def add_patient(self, nurse_id):
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

        with open(self.patientfilename, "a") as file:
            file.write(f"{nurse_id}, {patient_id}, {patient_name}, {medicine}, {medicine_date}, {medicine_time.strftime('%H:%M:%S')}\n")

        print("Patient added successfully!")

    def view_patients(self, nurse_id):
        if not os.path.exists(self.patientfilename):
            print("FILE NOT FOUND")
            return

        patients = {}

        with open(self.patientfilename, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                if len(parts) == 6:
                    record_nurse_id, patient_id, patient_name, medicine, medicine_date, medicine_time = parts
                    if record_nurse_id == nurse_id:
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

    def view_patients_by_id(self, nurse_id):
        if not os.path.exists(self.patientfilename):
            print("FILE NOT FOUND")
            return

        patients = {}

        with open(self.patientfilename, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                if len(parts) == 6:
                    record_nurse_id, patient_id, patient_name, medicine, medicine_date, medicine_time = parts
                    if record_nurse_id == nurse_id:
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

    def remove_patients(self, nurse_id, patient_to_remove):
        if not os.path.exists(self.patientfilename):
            print("FILE NOT FOUND")
            return

        patients = []

        with open(self.patientfilename, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                if len(parts) == 6:
                    record_nurse_id, patient_id, patient_name, medicine, medicine_date, medicine_time = parts
                    patients.append((record_nurse_id, patient_id, patient_name, medicine, medicine_date, medicine_time))

        patients = [patient for patient in patients if not (patient[1] == patient_to_remove and patient[0] == nurse_id)]

        with open(self.patientfilename, "w") as file:
            for record_nurse_id, patient_id, patient_name, medicine, medicine_date, medicine_time in patients:
                file.write(f"{record_nurse_id}, {patient_id}, {patient_name}, {medicine}, {medicine_date}, {medicine_time}\n")

        print("The patient record has been removed")

class       NurseAccess(PatientRecord):
    def __init__(self, nursefilename="nurses.txt", patientfilename="patients.txt"):
        super().__init__(patientfilename)
        self.nursefilename = nursefilename

    def get_existing_nurse_ids(self):
        if not os.path.exists(self.nursefilename):
            return set()

        with open(self.nursefilename, "r") as file:
            nurses = file.readlines()

        existing_ids = set()
        for nurse in nurses:
            if nurse.strip():
                nurse_id, *_ = nurse.strip().split(", ", 1)
                existing_ids.add(nurse_id)

        return existing_ids

    def add_nurse(self):
        existing_ids = self.get_existing_nurse_ids()
        nurse_id = input("Register nurse id: ")

        if nurse_id in existing_ids:
            print("Nurse ID already exists. Please use a unique ID.")
            return

        nurse_name = input("Enter nurse's name: ").title()
        password = input("Enter password: ")

        with open(self.nursefilename, "a") as file:
            file.write(f"{nurse_id}, {nurse_name}, {password}\n")

        print(f"\nWelcome to the hospital Nurse {nurse_name}!")

    def main_access(self):
        validate = Validation(self.nursefilename)

        nurse_id = input("Enter your nurse id: ")
        password = input("Enter your password: ")

        if validate.log_in(nurse_id, password):
            print("\nLogged in successfully")

            print("\nNurse Main Access")
            while True:
                print("\n1. Add patient")
                print("2. Remove patient")
                print("3. View All patients")
                print("4. View patient by their ID")
                print("5. Log out\n")

                choice = input("Please enter your choice: ")

                if choice == '1':
                    self.add_patient(nurse_id)
                elif choice == '2':
                    patient_id = input("Enter the patient ID to remove: ")
                    self.remove_patients(nurse_id, patient_id)
                elif choice == '3':
                    self.view_patients(nurse_id)
                elif choice == '4':
                    self.view_patients_by_id(nurse_id)
                elif choice == '5':
                    print("\nLogging Out...")
                    break
                else:
                    print("\nInvalid choice. Please enter a valid option.\n")
        else:
            print("Invalid credentials. Please try again or please sign up first.")

class Validation:
    def __init__(self, nursefilename):
        self.nursefilename = nursefilename

    def log_in(self, nurse_id, password):
        if not os.path.exists(self.nursefilename):
            print("FILE NOT FOUND")
            return False

        with open(self.nursefilename, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                if len(parts) == 3:
                    stored_id, _, stored_password = parts
                    if stored_id == nurse_id and stored_password == password:
                        return True
        return False

def main():
    nursefilename = "nurses.txt"
    access = NurseAccess(nursefilename)

    print("\nWelcome to Patient's Medicine Tracker")
    while True:
        print("\n1. Log in")
        print("2. Sign up")
        print("3. Exit\n")

        choice1 = input("Please enter your choice: ")

        if choice1 == '1':
            access.main_access()
        elif choice1 == '2':
            access.add_nurse()
        elif choice1 == '3':
            print("\nThank you for your hard work")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.\n")

if __name__ == '__main__':
    main()

