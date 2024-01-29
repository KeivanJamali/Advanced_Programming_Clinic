from tabulate import tabulate


class Notification:
    def send_notification_successful(self):
        """Send successful notification"""
        pass

    def send_notification_unsuccessful(self):
        """Send unsuccessful notification"""
        pass

    def make_table_doctor(self, doctor, doctor_schedule: list) -> None:
        """
        Generate a table for a given doctor and their schedule.

        Parameters:
            doctor (Doctor): The doctor object containing the doctor's information.
            doctor_schedule (list): A list of dictionaries representing the doctor's schedule. Each dictionary contains
            the date, time, clinic, patient name, and patient phone number.

        Returns:
            None

        This function takes a doctor object and their schedule, and generates a table to display the schedule.
        The schedule is converted to a 2D list, with each row representing a schedule entry. The table is then displayed
        using the tabulate function from the tabulate library, with the specified headers and formatting options.
        """
        data = []
        for row in doctor_schedule:
            sub = [row["date"], row["time"], row["clinic"], row["patient_name"], row["patient_phone_number"]]
            data.append(sub)

        headers = ["Date", "Time", "Clinic", "Patient Name", "Patient Phone Number"]

        print(f"### Doctor {doctor.first_name} {doctor.last_name}" + f" Phone number: {doctor.phone_number} ###")
        print(tabulate(data, headers=headers, tablefmt="fancy_grid", showindex="always", numalign="center"))

    def make_table_clinic(self, clinic, clinic_appointment: list) -> None:
        """
        Generates a table for a given clinic and clinic appointment data.

        Parameters:
            clinic (Clinic): The clinic object containing information about the clinic.
            clinic_appointment (list): A list of appointment data for the clinic.

        Returns:
            None

        This function takes a clinic object and a list of clinic appointment data and generates a table. The table is
        printed to the console using the tabulate library. Each row of the table represents an appointment and contains
        the following columns:
        - Date: The date of the appointment
        - Time: The time of the appointment
        - Doctor Name: The name of the doctor for the appointment
        - Doctor Phone Number: The phone number of the doctor for the appointment
        - Patient Name: The name of the patient for the appointment
        - Patient Phone Number: The phone number of the patient for the appointment

        The table is generated by iterating over the clinic appointment data and constructing a list of sublists, where
        each sublist represents a row in the table. The sublists are then added to the 'data' list. The headers for
        the table are defined in the 'headers' list.

        After the table is generated, additional information about the clinic is printed to the console, including
        the clinic name, address, and secretary phone number.
        """
        data = []
        for row in clinic_appointment:
            sub = [row["date"], row["time"], row["doctor_name"], row["doctor_phone_number"], row["patient_name"],
                   row["patient_phone_number"]]
            data.append(sub)
        headers = ["Date", "Time", "Doctor Name", "Doctor Phone Number", "Patient Name", "Patient Phone Number"]
        print(
            f"Clinic {clinic.clinic_name}" + f"Address: {clinic.address}" + f"Secretary Phone Number: {clinic.secretary_phone_number}")
        print(tabulate(data, headers=headers, tablefmt="fancy_grid", showindex="always", numalign="center"))

    def make_table_current_appointment(self,patient ,current_appointments):
        data = []
        for row in current_appointments:
            sub = [row["Date"], row["Time"], row["Doctor Name"], row["Clinic Name"]]
            data.append(sub)

        headers = ["Date", "Time", "Doctor Name", "Clinic Name"]
        print(f"Patient: {patient.first_name} {patient.last_name} | phone number: {patient.phone_number}")
        print(tabulate(data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def make_table_appointment(self,patient ,appointments_history):
        headers = ["Date", "Time", "Doctor Name", "Clinic Name"]
        print(f"Patient: {patient.first_name} {patient.last_name} | phone number: {patient.phone_number}")
        print(tabulate(appointments_history, headers=headers, tablefmt="fancy_grid", numalign="center"))

