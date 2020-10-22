class Student:
    roll = ""
    gpa = ""

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def disply(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


karim = Student()
karim.set_value(101,3.90)
karim.disply()

rahim = Student()
rahim.set_value(102,3.95)
rahim.disply()


