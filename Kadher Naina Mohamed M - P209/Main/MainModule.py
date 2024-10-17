import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.DBConnUtil import *
from util.DBPropertyUtil import *
from dao.Hospital_Service import *
from dao.HospitalSeviceImp import *

class MainModule:
    con = DBConnUtil.getConnObj(DBPropertyUtil.getConnectionStr())
    cursor = con.cursor()
    obj = HospitalService()

    while(True):
        print("Enter 1 to get appointments by id")
        print("Enter 2 to get appointments for patients")
        print("Enter 3 to get appointments for doctor")
        print("Enter 4 to schedule appointmets")
        print("Enter 5 to update appointments")
        print("Enter 6 to cancel appointments")
        print("Enter 0 to exit")

        choice = int(input("Enter Your choice : "))
        if(choice == 0):
            break
        elif choice == 1:
            print(obj.get_appointment_by_id(con))
        elif choice == 2:
            print(obj.get_appointments_for_patient(con))
        elif choice == 3:
            print(obj.get_appointments_for_doctor(con))
        elif choice == 4:
            obj.schedule_appointment(con)
        elif choice == 5:
            obj.update_appointment(con)
        elif choice == 6:
            obj.cancel_appointment(con)

