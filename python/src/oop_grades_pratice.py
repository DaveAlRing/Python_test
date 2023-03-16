class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100
        
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False
        
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
        
dave = Student("Dave", 32, 93)
teagan = Student("Teagan", 7, 95)
jena = Student("Jena", 28, 94)

math = Course("Math", 3)

math.add_students(dave)
math.add_students(teagan)
math.add_students(jena)

print(math.get_average_grade())
        


