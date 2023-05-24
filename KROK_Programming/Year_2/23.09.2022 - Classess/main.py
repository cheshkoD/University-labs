class Student:

    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name}'


class Group:

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __str__(self):
        return self.name + '\n' + '\n'.join(map(str, self.students))


st_1 = Student("Cheshko","Dmytro")
st_2 = Student("Bodnya","Andrey")

group_1 = Group("KN-21")
group_1.add_student(st_1)
group_1.add_student(st_2)

print(st_1)
print(group_1)