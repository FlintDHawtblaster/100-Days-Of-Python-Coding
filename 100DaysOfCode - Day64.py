#Object-Oriented Programming in Python. Yayyy!!
class job:
    name = None
    salary = None
    hoursWorked = None
    
    def __init__(self, name, salary, hoursWorked):
        self.name = name
        self.salary = float(salary)
        self.hoursWorked = int(hoursWorked)
    
    def display(self):    
        print(f"""{self.name} - ${self.salary} - {self.hoursWorked}hrs\n""")
        
class doctor(job):
    experience = None
    specialty = None
    
    def __init__(self, experience, specialty):
        self.name = "Doctor"
        self.salary = 120000.00
        self.hoursWorked = 375
        self.experience = experience
        self.specialty = specialty
        
    def show(self):    
        print(f"""{self.name} - ${self.salary} - {self.hoursWorked}hrs
                experience: {self.experience}
                specialty: {self.specialty}\n""")
        
class teacher(job):
    subject = None
    position = None
    
    def __init__(self, subject, position):
        self.name = "Teacher"
        self.salary = 100000.00
        self.hoursWorked = 248
        self.subject = subject
        self.position = position
    
    def outpour(self):    
            print(f"""{self.name} - ${self.salary} - {self.hoursWorked}hrs
                  experience: {self.subject}
                  specialty: {self.position}\n""")
        
lawyer = job("Lawyer", 250000.00, 120)
lawyer.display()

benjamin = doctor(7, "Paediatric Consultant")
benjamin.show()

teddy = teacher("Computer Science", "Teacher")
teddy.outpour()


