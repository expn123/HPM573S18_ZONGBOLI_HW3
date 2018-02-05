class Patient:
    def __init__(self,name):
        """
        :param name:Patient's name
        """
        self.name=name

    def discharge(self):
        """
        :return:print the name and type of the patient when called
        """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class EmergencyPatient(Patient):
    def __init__(self,name):

        Patient.__init__(self,name)
        self.costp=1000
    def discharge(self):
        type_emergency='emergency'
        dischargeout = [self.name, type_emergency]
        return dischargeout

class HospitalizedPatient(Patient):
    def __init__(self,name):
        Patient.__init__(self,name)
        self.costp=2000
    def discharge(self):
        type_hospital='hospitalized'
        dischargeout=[self.name,type_hospital]
        return dischargeout

class Hospital:
    def __init__(self,cost):
        self.cost=cost
    def admit(self,patients):
        self.patients=patients
    def discharge_all(self):
        discharge_alllist=[]
        for patient in self.patients:
            discharge_alllist.append(patient.discharge())
            self.cost+=patient.costp
        return discharge_alllist
    def get_total_cost(self):
        costtotal=0
        for patient in self.patients:
            costtotal+=patient.costp
        return costtotal

he=HospitalizedPatient("he")
bai=HospitalizedPatient("bai")
pan=EmergencyPatient("pan")
sa=EmergencyPatient("sa")
gui=EmergencyPatient("gui")
zhenpiaoliang=Hospital(0)
zhenpiaoliang.admit([he,bai,pan,sa,gui])
print(zhenpiaoliang.discharge_all())
print(zhenpiaoliang.get_total_cost())
print(zhenpiaoliang.cost)
