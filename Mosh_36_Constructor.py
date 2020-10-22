class Student:
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):   # Constructor
        self.roll = roll
        self.gpa = gpa

    def disply(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


karim = Student(101,3.95)
karim.disply()

rahim = Student(103,3.99)
rahim.disply()


