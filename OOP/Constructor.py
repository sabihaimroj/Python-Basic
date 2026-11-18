# Class
class Student:

    # default constructors
    def __init__(self):
        pass

    # parameterized cconstructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("new student.")


s1 = Student("Sabiha", 85)
print(s1.name)

s2 = Student("Tahmid", 88)
print(s2.name, s2.marks)
