# dao/ihospital_service.py

                                             
from abc import ABC, abstractmethod
from typing import List
from EntityClasses.entity import Appointment


class IHospitalService(ABC):

    @abstractmethod
    def get_appointment_by_id(self, con):
        
        pass

    @abstractmethod
    def get_appointments_for_patient(self, con):
       
        pass

    @abstractmethod
    def get_appointments_for_doctor(self, con):
       
        pass

    @abstractmethod
    def schedule_appointment(self, con):
        
        pass

    @abstractmethod
    def update_appointment(self, con):
        
        pass

    @abstractmethod
    def cancel_appointment(self, con):
        
        pass
