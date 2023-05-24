class Course(object):

    def __init__(self,course_number):
        self.course_number = int(course_number)
        self.students = []

    def get_course_number(self):
         print (self.course_number)

    def add_student(self, student_id):
        self.students.append(student_id)

    def drop_student(self, student_id):
        if student_id in self.students:
            self.students.remove(student_id)

    def get_roster(self):
        print (sorted(self.students))

    def show_students(self):
        print (self.students)


class Employee:

    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project

    def show(self):
        print("Name: ", self.name, 'Salary:', self.salary)

    def work(self):
        print(self.name, 'is working on', self.project)


