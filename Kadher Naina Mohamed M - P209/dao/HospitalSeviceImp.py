# dao/hospital_service.py

from typing import List
from EntityClasses.entity import Appointment
from dao.Hospital_Service import IHospitalService

class HospitalService(IHospitalService):
    def get_appointment_by_id(self, con):
        cursor = con.cursor()
        id = int(input("Enter id : "))
        appoint = cursor.execute("select * from Appointment where appointment_id=?", (id)).fetchone()
        return appoint

    def get_appointments_for_patient(self, con):
        cursor = con.cursor()
        id = int(input("Enter Patient_id : "))
        appoint = cursor.execute("select * from Appointment where patient_id=?", (id)).fetchall()
        return list(appoint)
        

    def get_appointments_for_doctor(self, con):
        cursor = con.cursor()
        id = int(input("Enter Doctor_id : "))
        appoint = cursor.execute("select * from Appointment where doctor_id=?", (id)).fetchall()
        return list(appoint)
        

    def schedule_appointment(self, con):
        cursor = con.cursor()
        app_id = int(input("Enter appointment id : "))
        patient_id = int(input("Enter Patient id : "))
        Doctor_id = int(input("Enter Doctor id : "))
        appointment_date = input("Enter appointmet date")
        Description = input("Enter description : ")

        cursor.execute("insert into Appointment values(?,?,?,?,?)", (app_id, patient_id, Doctor_id,
                                                                     appointment_date, Description))
        con.commit()

    def update_appointment(self, con):
        cursor = con.cursor()
        app_id = int(input("Enter appointment id : "))
        patient_id = int(input("Enter Patient id : "))
        Doctor_id = int(input("Enter Doctor id : "))
        appointment_date = input("Enter appointmet date")
        Description = input("Enter description : ")

        cursor.execute("update Appointment set patient_id=?,doctor_id=?,appointment_date=?,description=?", (patient_id,Doctor_id,appointment_date, Description))
        con.commit()
        

    def cancel_appointment(self, con):
        cursor = con.cursor()
        app_id = int(input("Enter appointment id : "))
        cursor.execute("delete from Appointment where appointment_id=?", (app_id))
        con.commit()
