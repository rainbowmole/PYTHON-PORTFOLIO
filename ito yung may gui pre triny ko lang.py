import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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

    def add_patient(self, patient_id, patient_name, medicine, medicine_date, medicine_time):
        existing_ids = self.get_existing_patient_ids()

        if patient_id in existing_ids:
            print("Patient ID already exists. Please use a unique ID.")
            return "Patient ID already exists."

        try:
            medicine_time = datetime.datetime.strptime(medicine_time, '%H:%M:%S')
        except ValueError:
            print("Invalid time format. Please enter time as HH:MM:SS.")
            return "Invalid time format. Please enter time as HH:MM:SS."

        with open(self.patientfilename, "a") as file:
            file.write(f"{patient_id}, {patient_name}, {medicine}, {medicine_date}, {medicine_time.strftime('%H:%M:%S')}\n")

        print("Patient added successfully!")
        return "Patient added successfully!"

    def view_patients(self):
        if not os.path.exists(self.patientfilename):
            print("FILE NOT FOUND")
            return "FILE NOT FOUND"

        patients = {}

        with open(self.patientfilename, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                if len(parts) == 5:
                    patient_id, patient_name, medicine, medicine_date, medicine_time = parts
                    if patient_id in patients:
                        patients[patient_id].append((patient_name, medicine, medicine_date, medicine_time))
                    else:
                        patients[patient_id] = [(patient_name, medicine, medicine_date, medicine_time)]

        patient_details = "\n ALL PATIENTS \n"
        for patient_id, patient_list in patients.items():
            patient_details += f"\nPatient ID: {patient_id}\n"
            for patient_name, medicine, medicine_date, medicine_time in patient_list:
                patient_details += (f"\tPatient's Name: {patient_name}"
                                    f"\n\tMedicine taking: {medicine}"
                                    f"\n\tTaking every: {medicine_date} at {medicine_time}\n")
        return patient_details

    def view_patients_by_id(self, patient_id):
        if not os.path.exists(self.patientfilename):
            print("FILE NOT FOUND")
            return "FILE NOT FOUND"

        patients = {}

        with open(self.patientfilename, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                if len(parts) == 5:
                    pid, patient_name, medicine, medicine_date, medicine_time = parts
                    if pid in patients:
                        patients[pid].append((patient_name, medicine, medicine_date, medicine_time))
                    else:
                        patients[pid] = [(patient_name, medicine, medicine_date, medicine_time)]

        filtered_patients = patients.get(patient_id, [])

        if not filtered_patients:
            print(f"Patient does not exist")
            return "Patient does not exist"
        else:
            patient_details = f"\nPatient {patient_id}\n"
            for patient_name, medicine, medicine_date, medicine_time in filtered_patients:
                patient_details += (f"\tPatient's Name: {patient_name}"
                                    f"\n\tMedicine: {medicine}"
                                    f"\n\tTaking every: {medicine_date} at {medicine_time}\n")
            return patient_details

class NurseAccess(PatientRecord):
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

    def add_nurse(self, nurse_id, nurse_name, password):
        existing_ids = self.get_existing_nurse_ids()

        if nurse_id in existing_ids:
            print("Nurse ID already exists. Please use a unique ID.")
            return "Nurse ID already exists."

        with open(self.nursefilename, "a") as file:
            file.write(f"{nurse_id}, {nurse_name}, {password}\n")

        print(f"\nWelcome to the hospital Nurse {nurse_name}!")
        return f"Welcome to the hospital Nurse {nurse_name}!"

    def main_access(self):
        validate = Validation(self.nursefilename)

        nurse_id = input("Enter your nurse id: ")
        password = input("Enter your password: ")

        if validate.log_in(nurse_id, password):
            print("\nLogged in successfully")

            print("\nNurse Main Access")
            while True:
                print("\n1. Add patient")
                print("2. View All patients")
                print("3. View patient by their ID")
                print("4. Log out\n")

                choice = input("Please enter your choice: ")

                if choice == '1':
                    self.add_patient()
                elif choice == '2':
                    self.view_patients()
                elif choice == '3':
                    self.view_patients_by_id()
                elif choice == '4':
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

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Patient's Medicine Tracker")
        self.geometry("500x400")

        self.nursefilename = "nurses.txt"
        self.patientfilename = "patients.txt"

        self.validation = Validation(self.nursefilename)
        self.nurse_access = NurseAccess(self.nursefilename, self.patientfilename)

        self.create_widgets()

    def create_widgets(self):
        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(pady=50)

        self.lbl_nurse_id = ttk.Label(self.login_frame, text="Nurse ID:")
        self.lbl_nurse_id.grid(row=0, column=0, padx=5, pady=5)

        self.entry_nurse_id = ttk.Entry(self.login_frame)
        self.entry_nurse_id.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_password = ttk.Label(self.login_frame, text="Password:")
        self.lbl_password.grid(row=1, column=0, padx=5, pady=5)

        self.entry_password = ttk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        self.btn_login = ttk.Button(self.login_frame, text="Login", command=self.login)
        self.btn_login.grid(row=2, columnspan=2, pady=5)

        self.lbl_result = ttk.Label(self.login_frame, text="")
        self.lbl_result.grid(row=3, columnspan=2, pady=5)

    def login(self):
        nurse_id = self.entry_nurse_id.get()
        password = self.entry_password.get()

        if self.validation.log_in(nurse_id, password):
            self.lbl_result.config(text="Login successful!")
            self.open_nurse_access()
        else:
            self.lbl_result.config(text="Invalid ID or password")

    def open_nurse_access(self):
        self.login_frame.pack_forget()
        self.nurse_frame = ttk.Frame(self)
        self.nurse_frame.pack(pady=50)

        self.btn_add_patient = ttk.Button(self.nurse_frame, text="Add Patient", command=self.add_patient)
        self.btn_add_patient.grid(row=0, column=0, padx=5, pady=5)

        self.btn_view_patients = ttk.Button(self.nurse_frame, text="View All Patients", command=self.view_patients)
        self.btn_view_patients.grid(row=1, column=0, padx=5, pady=5)

        self.btn_view_patient_by_id = ttk.Button(self.nurse_frame, text="View Patient by ID", command=self.view_patient_by_id)
        self.btn_view_patient_by_id.grid(row=2, column=0, padx=5, pady=5)

        self.btn_logout = ttk.Button(self.nurse_frame, text="Log Out", command=self.logout)
        self.btn_logout.grid(row=3, column=0, padx=5, pady=5)

    def add_patient(self):
        self.add_patient_frame = ttk.Frame(self)
        self.add_patient_frame.pack(pady=50)

        self.lbl_patient_id = ttk.Label(self.add_patient_frame, text="Patient ID:")
        self.lbl_patient_id.grid(row=0, column=0, padx=5, pady=5)
        self.entry_patient_id = ttk.Entry(self.add_patient_frame)
        self.entry_patient_id.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_patient_name = ttk.Label(self.add_patient_frame, text="Patient Name:").title()
        self.lbl_patient_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_patient_name = ttk.Entry(self.add_patient_frame)
        self.entry_patient_name.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_medicine = ttk.Label(self.add_patient_frame, text="Medicine:").title()
        self.lbl_medicine.grid(row=2, column=0, padx=5, pady=5)
        self.entry_medicine = ttk.Entry(self.add_patient_frame)
        self.entry_medicine.grid(row=2, column=1, padx=5, pady=5)

        self.lbl_medicine_date = ttk.Label(self.add_patient_frame, text="Medicine Date (Mon/Tues/Wed/Thurs/Fri/Sat/Sun):").title()
        self.lbl_medicine_date.grid(row=3, column=0, padx=5, pady=5)
        self.entry_medicine_date = ttk.Entry(self.add_patient_frame)
        self.entry_medicine_date.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_medicine_time = ttk.Label(self.add_patient_frame, text="Medicine Time (HH:MM:SS):")
        self.lbl_medicine_time.grid(row=4, column=0, padx=5, pady=5)
        self.entry_medicine_time = ttk.Entry(self.add_patient_frame)
        self.entry_medicine_time.grid(row=4, column=1, padx=5, pady=5)

        self.btn_save_patient = ttk.Button(self.add_patient_frame, text="Save Patient", command=self.save_patient)
        self.btn_save_patient.grid(row=5, columnspan=2, pady=5)

    def save_patient(self):
        patient_id = self.entry_patient_id.get()
        patient_name = self.entry_patient_name.get()
        medicine = self.entry_medicine.get()
        medicine_date = self.entry_medicine_date.get()
        medicine_time = self.entry_medicine_time.get()

        result = self.nurse_access.add_patient(patient_id, patient_name, medicine, medicine_date, medicine_time)
        messagebox.showinfo("Result", result)
        self.add_patient_frame.pack_forget()

    def view_patients(self):
        patients = self.nurse_access.view_patients()
        messagebox.showinfo("All Patients", patients)

    def view_patient_by_id(self):
        self.view_patient_id_frame = ttk.Frame(self)
        self.view_patient_id_frame.pack(pady=50)

        self.lbl_patient_id = ttk.Label(self.view_patient_id_frame, text="Enter Patient ID:")
        self.lbl_patient_id.grid(row=0, column=0, padx=5, pady=5)
        self.entry_patient_id_view = ttk.Entry(self.view_patient_id_frame)
        self.entry_patient_id_view.grid(row=0, column=1, padx=5, pady=5)

        self.btn_search_patient = ttk.Button(self.view_patient_id_frame, text="Search", command=self.search_patient_by_id)
        self.btn_search_patient.grid(row=1, columnspan=2, pady=5)

    def search_patient_by_id(self):
        patient_id = self.entry_patient_id_view.get()
        patient_details = self.nurse_access.view_patients_by_id(patient_id)
        messagebox.showinfo("Patient Details", patient_details)
        self.view_patient_id_frame.pack_forget()

    def logout(self):
        self.nurse_frame.pack_forget()
        self.create_widgets()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
