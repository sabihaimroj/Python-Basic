class Student:
    collegeName = "ABC College"  #class attribute

    def __init__(self, name, marks):
        self.name = name    # object attribute
        self.marks = marks  # object attribute
        print("new student.")


s1 = Student("Sabiha", 85)
print(s1.name)

s2 = Student("Tahmid", 88)
print(s2.name, s2.marks)

