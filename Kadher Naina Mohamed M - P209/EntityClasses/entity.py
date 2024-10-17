from datetime import datetime

class Patient:
    def __init__(self, patient_id=None, first_name=None, last_name=None, date_of_birth=None, gender=None, contact_number=None, address=None):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__contact_number = contact_number
        self.__address = address

    # Getters
    def get_patient_id(self):
        return self.__patient_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_gender(self):
        return self.__gender

    def get_contact_number(self):
        return self.__contact_number

    def get_address(self):
            return self.__address

    # Setters
    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_gender(self, gender):
        self.__gender = gender

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def set_address(self, address):
        self.__address = address

    # String representation
    def __str__(self):
        return (f"Patient(patientId={self.__patient_id}, "
                f"firstName='{self.__first_name}', "
                f"lastName='{self.__last_name}', "
                f"dateOfBirth={self.__date_of_birth}, "
                f"gender='{self.__gender}', "
                f"contactNumber='{self.__contact_number}'), "
                f"address='{self.__address}'")


class Doctor:
    def __init__(self, doctor_id=None, first_name=None, last_name=None, specialization=None, contact_number=None):
        self.__doctor_id = doctor_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__specialization = specialization
        self.__contact_number = contact_number

    # Getters
    def get_doctor_id(self):
        return self.__doctor_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_specialization(self):
        return self.__specialization

    def get_contact_number(self):
        return self.__contact_number

    # Setters
    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    # String representation
    def __str__(self):
        return (f"Doctor(doctorId={self.__doctor_id}, "
                f"firstName='{self.__first_name}', "
                f"lastName='{self.__last_name}', "
                f"specialization='{self.__specialization}', "
                f"contactNumber='{self.__contact_number}')")


class Appointment:
    def __init__(self, appointment_id=None, patient_id=None, doctor_id=None, appointment_date=None, description=None):
        self.__appointment_id = appointment_id
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__appointment_date = appointment_date
        self.__description = description

    # Getters
    def get_appointment_id(self):
        return self.__appointment_id

    def get_patient_id(self):
        return self.__patient_id

    def get_doctor_id(self):
        return self.__doctor_id

    def get_appointment_date(self):
        return self.__appointment_date

    def get_description(self):
        return self.__description

    # Setters
    def set_appointment_id(self, appointment_id):
        self.__appointment_id = appointment_id

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id

    def set_appointment_date(self, appointment_date):
        self.__appointment_date = appointment_date

    def set_description(self, description):
        self.__description = description

    # String representation
    def __str__(self):
        return (f"Appointment(appointmentId={self.__appointment_id}, "
                f"patientId={self.__patient_id}, "
                f"doctorId={self.__doctor_id}, "
                f"appointmentDate={self.__appointment_date}, "
                f"description='{self.__description}')")

