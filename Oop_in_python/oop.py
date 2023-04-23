# student ={ "name" : "Neeraj" , "grades" : (89, 78, 90, 67, 89)}



# def average(sequence):  # Here we are passing one parameter
#     return sum(sequence)/len(sequence)



# print( average(student["grades"])) #here we are passing one argument

class Student :
    def __init__(self):
        self.name = "Neeraj Appa"
        self.grade = ( 90, 89, 56, 79, 45)

    def average(self):
        return sum(self.grade)/ len(self.grade)

student = Student()

print(student.name )
print(student.grade)
print(Student.average(student))
